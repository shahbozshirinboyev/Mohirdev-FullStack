from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # ⚠️ MUHIM: super().save_user() chaqirmaymiz, chunki u ichida ._has_phone_field ishlatiladi
        # O'zimiz bajaramiz
        data = getattr(form, 'cleaned_data', {})

        user.email = data.get('email', '')
        user.username = data.get('username', '')
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')

        if commit:
            user.save()
        return user