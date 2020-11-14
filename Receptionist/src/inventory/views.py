from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import datetime
from .models import MedicineData

# Create your views here.
class Inventory:

    @csrf_exempt
    def dashboard(self, request):
        return render(request, 'medi.html', {})

    @csrf_exempt
    def stocks(self, request):
        return render(request, 'add.html', {})

    @csrf_exempt
    def update_stocks(self, request):
        if request.method == "POST":
            med_name = request.POST.get('medicine') 
            batch_no = request.POST.get('batch')
            mf_date = request.POST.get('mfdate')
            no_of_boxes = request.POST.get('boxes')
            exp_date = request.POST.get('exdate')
            invoice_no = request.POST.get('invoice')
            no_of_pieces = request.POST.get('pieces')
            purchase_date = request.POST.get('purchase')

        
        try:
            # saving data here
            med = MedicineData(username=request.user.username, medicine_name=med_name,
                                batch_id=batch_no, mfd=mf_date, 
                                number_of_boxes=no_of_boxes,exd=exp_date, 
                                invoice_no=invoice_no, no_of_pieces=no_of_pieces,
                                date_of_purchase=purchase_date, date_of_added=datetime.datetime.now(),
                            )
            med.save()

            if med is not None:
                # med.no_of_days_left = str(med.exd - datetime.datetime.now().date())
                # med.save()
                return render(request, 'medi.html')
        except: pass
        return HttpResponse("failed")

    @csrf_exempt
    def show_medicines(self, request):
        obj = MedicineData.objects.all().order_by('medicine_name')
        context = {
            "meds": obj,
        }
        return render(request, 'inv.html', context)

    @csrf_exempt
    def expiring_list(self, request):
        obj = MedicineData.objects.all().order_by('exd')
        for data in obj:
            data.no_of_days_left = str(data.exd - datetime.datetime.now().date())
            data.save()
        context = {
            "meds": obj,
        }
        return render(request, 'exp.html', context)

    @csrf_exempt
    def shortage_list(self, request):
        obj = MedicineData.objects.all().order_by('no_of_pieces')
        context = {
            "meds": obj,
        }
        return render(request, 'short.html', context)