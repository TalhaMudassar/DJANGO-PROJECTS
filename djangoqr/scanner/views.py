from django.shortcuts import render
from .models import QRCode
import qrcode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
from pyzbar.pyzbar import decode
from PIL import Image
import os
import shutil


def generate_qr(request):
    qr_image_url = None
    if request.method == 'POST':
        mobile_number = request.POST.get('mobile_number')
        data = request.POST.get('qr_data')

        # Validate the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/generate.html', {'error': 'Invalid mobile number'})

        # Generate the QR code image with data and mobile number
        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)
        qr_image_io = BytesIO()
        qr.save(qr_image_io, format='PNG')
        qr_image_io.seek(0)

        # Define the storage location for the QR code images
        qr_storage_path = settings.MEDIA_ROOT / 'qr_codes'
        fs = FileSystemStorage(location=qr_storage_path, base_url='/media/qr_codes/')
        filename = f"{data}_{mobile_number}.png"
        qr_image_content = ContentFile(qr_image_io.read(), name=filename)
        fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

        # Save the QR code data and mobile number in the database
        QRCode.objects.create(data=data, mobile_number=mobile_number)
    return render(request, 'scanner/generate.html', {'qr_image_url': qr_image_url})


def scan_qr(request):
    result = None
    if request.method == 'POST' and request.FILES.get('qr_image'):
        mobile_number = request.POST.get('mobile_number')
        qr_image = request.FILES['qr_image']

        # Validate the mobile number
        if not mobile_number or len(mobile_number) != 10 or not mobile_number.isdigit():
            return render(request, 'scanner/scan.html', {'error': 'Invalid mobile number'})

        try:
            # Process the image directly from memory without saving it first
            image = Image.open(qr_image)
            decoded_objects = decode(image)
            image.close()  # Close the image immediately

            if decoded_objects:
                # Get the data from the first decoded object
                qr_content = decoded_objects[0].data.decode('utf-8').strip()
                qr_data, qr_mobile_number = qr_content.split('|')

                # Check if the data exists in the QRCode model with the provided mobile number
                qr_entry = QRCode.objects.filter(
                    data=qr_data, mobile_number=qr_mobile_number).first()

                if qr_entry and qr_mobile_number == mobile_number:
                    result = "✅ Scan Success: Valid QR Code"

                    # Delete the specific QR code entry from the database
                    qr_entry.delete()

                    # Move the QR code image to a deleted folder instead of deleting
                    qr_image_path = settings.MEDIA_ROOT / 'qr_codes' / f"{qr_data}_{qr_mobile_number}.png"
                    deleted_folder = settings.MEDIA_ROOT / 'deleted_qr_codes'
                    
                    # Create deleted folder if it doesn't exist
                    deleted_folder.mkdir(exist_ok=True)
                    
                    if qr_image_path.exists():
                        try:
                            # Move the file instead of deleting it
                            destination = deleted_folder / f"{qr_data}_{qr_mobile_number}.png"
                            shutil.move(str(qr_image_path), str(destination))
                            result += " - QR image moved to deleted folder"
                        except Exception as e:
                            result += " - Could not move QR image (file may be in use)"
                    else:
                        result += " - QR image not found"

                else:
                    result = "❌ Scan Failed: Invalid QR Code or mobile number mismatch"
            else:
                result = "⚠️ No QR Code detected in the image."
                
        except Exception as e:
            result = f"Error processing the image: {str(e)}"
            
    return render(request, 'scanner/scan.html', {'result': result})