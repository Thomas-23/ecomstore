
from django.views.generic import DetailView, View, ListView

#from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404, render
from models import Category, Product
from django.template import RequestContext


class IndexView(View):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    template_name = "catalog/index.html"

    def get(self, request):
        #return HttpResponse( self.page_title)
        return render(request, self.template_name, {"page_title": self.page_title})


'''
class ShowCategoryView(DetailView):
    template_name = "catalog/category.html"
    model = Category
    context_object_name = 'catogory'
'''

'''
    def get_object(self, queryset=None):
        print self.get_slug_field()
        return get_object_or_404(Category, slug=self.get_slug_field())
'''
'''
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ShowCategoryView, self).get_context_data(**kwargs)  # Add in a QuerySet of all the books
        #context['meta_keywords'] = Category.object.meta_keywords
        #context['meta_description'] = Category.object.meta_description
        return context
'''

'''
	def get_context_data( self, **kwargs):
		category = get_object_or_404(Category, slug=kwargs.category_slug)
		# Call the base implementation first to get a context
		context = super(ShowCategoryView, self ).get_context_data(**kwargs)
		# Add in the publisher
		context['products'] = category.product_set.all()
		context['meta_keywords'] = category.meta_keywords
		context['page_title'] = category.name
		context['meta_description'] = category.meta_description
		return context
'''


def show_category(request, slug, template_name="catalog/category.html"):
	c = get_object_or_404(Category, slug=slug)
	content = {"products":c.product_set.all(),"page_title":c.name,"meta_keywords":c.meta_keywords,"meta_description":c.meta_description,"description":c.description}
	return render(request,template_name,content)

'''
class ShowProductView(DetailView):
    template_name = "catalog/product.html"
    context_object_name = 'product'
    queryset = get_object_or_404(Product, is_active = True)
'''
'''
    def get_object(self, queryset= get_object_or_404(Product, is_active = True)):
        object = super(ShowProductView, self).get_object()
        return object
'''
'''
    def get_queryset(self):
        self.product = get_object_or_404(Product, is_active = True)
        return Product.object.filter(product=self.product)
'''


def show_product(request, slug, template_name="catalog/product.html"):
	p = get_object_or_404(Product, slug=slug)
	content = {"categories":p.categories.filter(is_active=True),"page_title":p.name,"meta_keywords":p.meta_keywords,"meta_description":p.meta_description,'p':p }
	return render(request,template_name,content)

