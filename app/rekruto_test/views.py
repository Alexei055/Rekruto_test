from django.shortcuts import render


def test_view(request):
    name = request.GET.get("name", False)
    message = request.GET.get("message", False)

    if name and message:
        context = {
            'name': name,
            'message': message
        }

        return render(request=request, template_name='rekruto_test/next_page.html', context=context)

    else:

        return render(request=request, template_name='rekruto_test/first_page.html')
