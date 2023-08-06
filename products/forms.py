from django import forms

from products.models import Review, Product


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'text']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'title', 'compound', 'category']