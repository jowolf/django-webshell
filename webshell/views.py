import sys, StringIO

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required


@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    source = request.POST.get('source', '').replace('"', r'\"')

    sys.stdout = StringIO.StringIO()
    sys.stderr = StringIO.StringIO()

    try:
        exec source
    except Exception, e:
        print e

    result = 'stdout: \n%s\n\nstderr: \n%s' % (sys.stdout.getvalue(), sys.stderr.getvalue())

    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    return HttpResponse(result)
    
