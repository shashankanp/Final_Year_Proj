from django import forms
from django.db import transaction

from .models import NewsAndEvents, Session, Semester, SEMESTER
from django.apps import AppConfig
# from web3 import Web3

# ganache_url = "http://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))

# account_1 = "0x0fA698262632eCceeA0c65C10BA28CF0A5f5d4Dc"
# account_2 = "0x956310A9DE356ac85C0E0748BE44AD49bFe909D4"

# private_key = "0xbf543a548fd0bcbcbae59e1213a128515164cd86d5719b6e7a5c8e56d4a08b56"

# nonce = web3.eth.get_transaction_count(account_1)

# tx = {
#     'nonce': nonce,
#     'to': account_2,
#     'value': web3.to_wei(1, 'ether'),
#     'gas': 2000000,
#     'gasPrice': web3.to_wei('50', 'gwei'),
# }

# signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# print(web3.to_hex(tx_hash))
# print("Transaction succesfull!")


# news and events
class NewsAndEventsForm(forms.ModelForm):
    class Meta:
        model = NewsAndEvents
        fields = ('title', 'summary', 'posted_as',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['posted_as'].widget.attrs.update({'class': 'form-control'})


class SessionForm(forms.ModelForm):
    next_session_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
            }
        ),
        required=True)

    class Meta:
        model = Session
        fields = ['session', 'is_current_session', 'next_session_begins']


class SemesterForm(forms.ModelForm):
    semester = forms.CharField(
        widget=forms.Select(
            choices=SEMESTER,
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="semester",
    )
    is_current_semester = forms.CharField(
        widget=forms.Select(
            choices=((True, 'Yes'), (False, 'No')),
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        label="is current semester ?",
    )
    session = forms.ModelChoiceField(
        queryset=Session.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'browser-default custom-select',
            }
        ),
        required=True
    )

    next_semester_begins = forms.DateTimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
            }
        ),
        required=True)

    class Meta:
        model = Semester
        fields = ['semester', 'is_current_semester',
                  'session', 'next_semester_begins']
