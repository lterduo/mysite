# flex





```css
.box{
  display: flex;
}
```

行内元素也可以使用 Flex 布局。

> ```css
> .box{
>   display: inline-flex;
> }
> ```

Webkit 内核的浏览器，必须加上`-webkit`前缀。

> ```css
> .box{
>   display: -webkit-flex; /* Safari */
>   display: flex;
> }
> ```

注意，设为 Flex 布局以后，子元素的`float`、`clear`和`vertical-align`属性将失效。



以下6个属性设置在容器上。

* flex-direction

  * 设置主轴方向

    * ~~~
      row | row-reverse | column | column-reverse
      ~~~

* justify-content

  * 设置主轴上子元素的排列方式

  * 使用前一定要确认好主轴是哪个

  * 属性值：

    * ~~~
      flex-start | flex-end | center | space-between | space-around
      ~~~

* flex-wrap

  * 设置子元素是否换行，默认不换行，如果装不开，会缩小子元素的宽度

  * 属性值

    * ~~~
      nowrap | wrap | wrap-reverse
      ~~~

* align-items

  * 设置侧轴上的子元素的排列方式	适用单行

  * 属性值

    * ~~~
      align-items: flex-start | flex-end | center | baseline | stretch
      ~~~

* align-content

  * 设置侧轴上的子元素的排列方式	适用多行

  * 必须有换行，单行无效

  * 属性

    * ~~~
      flex-start | flex-end | center | space-between | space-around | stretch;
      ~~~

* flex-flow

  * flex-direction 和 flex-wrap 的缩写



以下6个属性设置在项目上。

* flex
  * 分配剩余空间，注意是剩余空间，用数字表示占多少份，默认是0不占用
  * 使用场景
    * 圣杯：三个盒子，左边有宽度flex：0，右边有宽度flex：0，中间flex：1，中间的占用所有的剩余空间
    * 三等分：三个盒子都没有宽度，直接flex：1，三等分
    * 根据设计，给各个盒子分配不同的flex数值
* align-self
  * 控制子元素自己在侧轴上的排列方式
  * 可覆盖align-item属性 
* order 
  * 控制子元素排列顺序
  * 默认值是0，数值越小越靠前！



# box-shadow

# border-radius

# border





*{

  box-sizing: border-box;

  margin: 0;

  padding: 0;

}



.container{

  width: 90%;

  background: #eee;

  margin: 50px auto;



}



# 伪选择器

a:hover {

​	color: red;

}

只有hover(盘旋)的时候才生效

 

# 浮动

1. normal flow：默认的一种排列方式
   （block-level elements)从上到下；(inline elements)从左到右
2. float：脱离normal flow，不排队
   	• 空间被后面的元素占用（相当于另起一个图层）；
      	• 不排队的人，也得排自己的队（多个元素浮动的情况）；
      	• 全部浮动，可实现横向排列；
      	• 父元素没有了浮动元素高度。
3. 清除浮动对后面元素magin-top的影响：
   ①在浮动后面元素的css中添加 clear:both;【上边距设置会无效显示】
   ②在浮动后面添加一个空的元素，css设置为 clear:both;【过于累赘】
   ③为浮动元素的父元素设置【最推荐】：
   .element::after{content:'';display:block;clear:both}
   可同时解决margin-top和父元素失去高度的问题。