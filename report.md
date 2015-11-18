
概要
===

> *资源文件变化情况*
> >	`新增`资源文件: `179` 个，共计 `1926268` 字节；<br/>
> >	`减少`资源文件: `50` 个，共计 `1855001` 字节；<br/>
> >	`原有`资源文件`大小增加`: `62` 个，共计 `62940` 字节；<br/>
> >	`原有`资源文件`大小下降`: `30` 个，共计 `15528` 字节； <br/>

>	总的来看，本次升级`资源文件`总大小 `增加`: `118679` 字节， `占比`: `0.45`％ <br/>  <!--同比：同上一个发布版本对比   环比：同上一次扫描进行对比-->


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
	
    <tr>
        <td>passenger/src/main/assets/tts/xiaoyan.jet</td>
        <td>5522</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/res/drawable-xhdpi/flier_popu_title.png</td>
        <td>471</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/res/drawable-xhdpi/ddrive_recruit_img.png</td>
        <td>443</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/res/drawable-xxhdpi/nova_driver_register_recommend_background.png</td>
        <td>426</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/res/drawable-xxhdpi/ic_splash_logo.png</td>
        <td>324</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/res/drawable-xxhdpi/common_btn_close_nine.png</td>
        <td>2073</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/res/raw-nodpi/new_home_intro.mp4</td>
        <td>2418</td>
        <td></td>
    </tr>
    	
</table>

## 大尺寸动态库
> Android工程 libs目录中超过`300KB`的`动态库`文件

<table>
	<tr>
		<th> 路径
		<th> 尺寸(KB)
		<th> 说明
	</tr>
	
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libtxmapengine.so</td>
        <td>321</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libdidipsgpush.so</td>
        <td>3449</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libwebpJNI.so</td>
        <td>353</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libdchat.so</td>
        <td>1101</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libsecbox.so</td>
        <td>317</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libmsc.so</td>
        <td>2645</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/src/main/jniLibs/armeabi/libDGBDynamicCrypt.so</td>
        <td>700</td>
        <td></td>
    </tr>
    	
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
	
    <tr>
        <td>passenger/libs/fastjson-1.2.7.jar</td>
        <td>407</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/libs/gson-2.3.1.jar</td>
        <td>205</td>
        <td></td>
    </tr>
    
    <tr>
        <td>passenger/libs/json-simple-1.1.1.jar</td>
        <td>23</td>
        <td></td>
    </tr>
    	
</table>	
