
概要
===

> *资源文件变化情况*
> >	`新增`资源文件: `%d` 个，共计 `%d` 字节；<br/>
> >	`减少`资源文件: `%d` 个，共计 `%d` 字节；<br/>
> >	`原有`资源文件`大小增加`: `%d` 个，共计 `%d` 字节；<br/>
> >	`原有`资源文件`大小下降`: `%d` 个，共计 `%d` 字节； <br/>

>	总的来看，本次升级`资源文件`总大小 `%s`: `%d` 字节， `占比`: `%.2f`％ <br/>  <!--同比：同上一个发布版本对比   环比：同上一次扫描进行对比-->


详情
===

重复资源问题
---
> 通过android lint扫描出个重复资源文件 <br/>

> 可删除文件列表情，参见附件的lint.html扫描结果 <br/>

大尺寸文件（资源文件、动态库、jar包）监控
---
> 分析android工程资源、动态库、jar的文件尺寸增长趋势，给出尺寸过大的文件列表。

## 大尺寸资源文件
> Android工程 assets、res目录中超过`300KB`的`资源`文件

<table>
	<tr>
		<th> 路径
		<th> 尺寸(KB)
		<th> 说明
	</tr>
	%s	
</table>

## 大尺寸动态库
> Android工程 libs目录中超过`300KB`的`动态库`文件

<table>
	<tr>
		<th> 路径
		<th> 尺寸(KB)
		<th> 说明
	</tr>
	%s	
</table>

## jar包
### 功能类似jar包
>  	Android工程libs目录下类似职能的jar包

<table>
	<tr>
		<th> 路径
		<th> 尺寸(KB)
		<th> 说明
	</tr>
	%s	
</table>	