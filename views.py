from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.shortcuts import render, redirect
from .forms import ShopForm


class eCommerceView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

def shop_create(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_list')  # Adjust the redirect to an appropriate page
    else:
        form = ShopForm()
    return render(request, 'app_ecommerce_settings_detail.html', {'form': form})
