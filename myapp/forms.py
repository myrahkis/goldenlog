from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from myapp.models import CreativeOrders


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CreativeOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['email'].label = "Почта"
        self.fields['typeOfWood'].label = "Вид дерева"
        self.fields['techTask'].label = "ТЗ"
        self.fields['exampleImg'].label = "Ваше фото"
        self.helper.form_action = reverse_lazy('home')

    class Meta:
        model = CreativeOrders
        fields = ['email', 'typeOfWood', 'techTask', 'exampleImg']

        widgets = {
            'techTask': forms.Textarea(attrs={'rows': 3}),
        }


    # CHOICES_PROD = [
    #     (CreativeOrders.PINE, 'Сосна'),
    #     (CreativeOrders.SPRUCE, 'Ель'),
    #     (CreativeOrders.ASPEN, 'Осина'),
    #     (CreativeOrders.BIRCH, 'Береза'),
    #     (CreativeOrders.BEECH, 'Бук'),
    #     (CreativeOrders.OAK, 'Дуб'),
    #     (CreativeOrders.ELM, 'Вяз'),
    #     (CreativeOrders.MAPLE, 'Клен'),
    #     (CreativeOrders.ASH, 'Ясень'),
    # ]
    #
    # email = forms.EmailField(label="Почта", required=True)
    # typeOfWood = forms.ChoiceField(choices=CHOICES_PROD, label="Вид дерева", required=True)
    # techTask = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label="Описание пожеланий", required=True)
    # exampleImg = forms.ImageField(label="Чертеж или эскиз", required=True)








