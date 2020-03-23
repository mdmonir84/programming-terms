# Django: How can I call a view function from template?

## One option is, you can wrap the submit button with a form

Something like this:

```
<form action="{% url path.to.request_page %}" method="POST">
    <input id="submit" type="button" value="Click" />
</form>
(remove the onclick and method)
```

If you want to load a specific part of the page, without page reload - you can do

```
<input id="submit" type="button" value="Click" data_url/>
```
and on a submit listener
```
$(function(){
     $('form').on('submit', function(e){
         e.preventDefault();
         $.ajax({
             url: $(this).attr('action'),
             method: $(this).attr('method'),
             success: function(data){ $('#target').html(data) }
         });
     });
});
```

## Alternative approach 

Assuming that you want to get a value from the user input in html textbox whenever the user clicks 'Click' button, and then call a python function (mypythonfunction) that you wrote inside mypythoncode.py. Note that "btn" class is defined in a css file.

```
inside templateHTML.html:

<form action="#" method="get">
 <input type="text" value="8" name="mytextbox" size="1"/>
 <input type="submit" class="btn" value="Click" name="mybtn">
</form>

inside view.py:

import mypythoncode

def request_page(request):
  if(request.GET.get('mybtn')):
    mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
return render(request,'myApp/templateHTML.html')
```
