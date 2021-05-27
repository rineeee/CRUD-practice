![](https://img.shields.io/badge/django-3.2.2-green)
![](https://img.shields.io/badge/HTML-pink)
![](https://img.shields.io/badge/CSS-blue)
![](https://img.shields.io/badge/JS-yellow)
![](https://img.shields.io/badge/Pillow-8.2.0-red)

# Django CRUD Practice Project
- CRUD 기반 연습용 프로젝트 입니다.

<br/>
<br/>

## CRUD

### 개념
- 데이터의 생성(Create), 조회(Read), 업데이트(Update), 삭제(Delete)를 말합니다.
- 서비스의 대부분의 기능에 적용되는 개념이기 때문에 확실히 공부하면 좋습니다!
<br/>
<br/>

### method structure

- Create
```python
def new_post(request):
    """
    "post"method로 들어온 request data를 받아서 객체를 생성합니다.
    ex) Post.objects.create(
                title=request.POST['title']
                )
    """
    return render()
```
- Read
```python
def post_detail(request, pk):
    """
    pk는 post 객체의 고유의 id값입니다.
    이 pk를 통해서 객체를 가져옵니다.
    ex) post = get_object_or_404(Post, id=pk)
    """
    return render()
```
- Update
```python
def post_update(request, pk):
        """
    "post"method로 들어온 request data를 받아서 객체를 업데이트 합니다.
    ex) Post.objects.get(id = pk)
        ...
        post.save()  # 수정된 사항을 저장합니다.        
    """
    return render()
```
- Delete
```python
def post_delete(request, pk):
    """
    post = Post.objects.get(id=pk)
    post.delete()  # post 객체를 삭제합니다.
    """
    return render()
```
<br/>
<br/>

## 보충설명
### get_object_or_404
```python
get_object_or_404(MODEL_NAME, pk=id)
```
- pk가 id에 해당하는 객체를 가지고 옵니다.<br>
- 만약에 해당객체가 없다면 404 에러 페이지를 띄웁니다.

### path converter
```python
path('blog/<int:id>', blogpost.views.detail, name="detail")
```
- 여러 객체들을 다루는, 계층적인 url을 자동생성할때 편리합니다.
- 함수에게 넘기는 인자로 몇 번 객체를 다룰 것인지에 대한 정보입니다.
- why use? 우리가 각 블로그 게시글들마다 path를 하나씩 추가하면 너무 불편하기 때문!
만약 1000개의 detail 페이지가 있다고 하면 우리가 일일이 1000개의 path를 만들어주면 너무 비효율적이기 때문입니다.

### POST vs GET
- POST : 데이터를 서버로 제출하여 추가 또는 수정하기 위해서 데이터를 전송하는 방식
- GET : 어떠한 정보를 가져와서 조회를 하기 위한 방식
- 장단점은 검색을 한번 해보세용!!




