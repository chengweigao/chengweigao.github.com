htaccess文件(或者”分布式配置文件”）提供了针对目录改变配置的方法， 即，在一个特定的文档目录中放置一个包含一个或多个指令的文件， 以作用于此目录及其所有子目录。作为用户，所能使用的命令受到限制。管理员可以通过Apache的AllowOverride指令来设置。

概述来说，htaccess文件是Apache服务器中的一个配置文件，它负责相关目录下的网页配置。通过htaccess文件，可以帮我们实现：网页301重定向、自定义404错误页面、改变文件扩展名、允许/阻止特定的用户或者目录的访问、禁止目录列表、配置默认文档等功能。

.htaccess 详解

.htaccess是什么

启用.htaccess，需要修改httpd.conf，启用AllowOverride，并可以用AllowOverride限制特定命令的使用。如果需要使用.htaccess以外的其他文件名，可以用AccessFileName指令来改变。例如，需要使用.config ，则可以在服务器配置文件中按以下方法配置：AccessFileName .config 。

笼统地说，.htaccess可以帮我们实现包括：文件夹密码保护、用户自动重定向、自定义错误页面、改变你的文件扩展名、封禁特定IP地址的用户、只允许特定IP地址的用户、禁止目录列表，以及使用其他文件作为index文件等一些功能。

工作原理

.htaccess文件(或者”分布式配置文件”)提供了针对每个目录改变配置的方法，即在一个特定的目录中放置一个包含指令的文件，其中的指令作用于此目录及其所有子目录。
说明：
如果需要使用.htaccess以外的其他文件名，可以用AccessFileName指令来改变。例如，需要使用.config ，则可以在服务器配置文件中按以下方法配置：
AccessFileName .config
通常，.htaccess文件使用的配置语法和主配置文件一样。AllowOverride指令按类别决定了.htaccess文件中哪些指令才是有效的。如果一个指令允许在.htaccess中使用，那么在本手册的说明中，此指令会有一个覆盖项段，其中说明了为使此指令生效而必须在AllowOverride指令中设置的值。

(不)使用.htaccess文件的场合

一般情况下，不应该使用.htaccess文件，除非你对主配置文件没有访问权限。有一种很常见的误解，认为用户认证只能通过.htaccess文件实现，其实并不是这样，把用户认证写在主配置文件中是完全可行的，而且是一种很好的方法。
.htaccess文件应该被用在内容提供者需要针对特定目录改变服务器的配置而又没有root权限的情况下。如果服务器管理员不愿意频繁修改配置，则可以允许用户通过.htaccess文件自己修改配置，尤其是ISP在同一个机器上运行了多个用户站点，而又希望用户可以自己改变配置的情况下。
虽然如此，一般都应该尽可能地避免使用.htaccess文件。任何希望放在.htaccess文件中的配置，都可以放在主配置文件的<Directory>段中，而且更高效。
避免使用.htaccess文件有两个主要原因。
首先是性能。如果AllowOverride启用了.htaccess文件，则Apache需要在每个目录中查找.htaccess文件，因此，无论是否真正用到，启用.htaccess都会导致性能的下降。另外，对每一个请求，都需要读取一次.htaccess文件。
还有，Apache必须在所有上级的目录中查找.htaccess文件，以使所有有效的指令都起作用(参见指令的生效)，所以，如果请求/www/htdocs/example中的页面，Apache必须查找以下文件：
/.htaccess /www/.htaccess /www/htdocs/.htaccess /www/htdocs/example/.htaccess
总共要访问4个额外的文件，即使这些文件都不存在。(注意，这可能仅仅由于允许根目录”/”使用.htaccess ，虽然这种情况并不多。)

其次是安全。这样会允许用户自己修改服务器的配置，这可能会导致某些意想不到的修改，所以请认真考虑是否应当给予用户这样的特权。但是，如果给予用户较少的特权而不能满足其需要，则会带来额外的技术支持请求，所以，必须明确地告诉用户已经给予他们的权限，说明AllowOverride设置的值，并引导他们参阅相应的说明，以免日后生出许多麻烦。
注意，在/www/htdocs/example目录下的.htaccess文件中放置指令，与在主配置文件中<Directory /www/htdocs/example>段中放置相同指令，是完全等效的。

/www/htdocs/example目录下的.htaccess文件的内容：
AddType text/example .exm
httpd.conf文件中摘录的内容：
<Directory /www/htdocs/example>
AddType text/example .exm
</Directory>
但是，把配置放在主配置文件中更加高效，因为只需要在Apache启动时读取一次，而不是在每次文件被请求时都读取。
将AllowOverride设置为none可以完全禁止使用.htaccess文件：
AllowOverride None

指令的作用范围

.htaccess文件中的配置指令作用于.htaccess文件所在的目录及其所有子目录，但是很重要的、需要注意的是，其上级目录也可能会有.htaccess文件，而指令是按查找顺序依次生效的，所以一个特定目录下的.htaccess文件中的指令可能会覆盖其上级目录中的.htaccess文件中的指令，即子目录中的指令会覆盖父目录或者主配置文件中的指令。

疑难解答

如果在.htaccess文件中的某些指令不起作用，可能有多种原因。
最常见的原因是AllowOverride指令没有被正确设置，必须确保没有对此文件区域设置 AllowOverride None 。有一个很好的测试方法，就是在.htaccess文件随便增加点无意义的垃圾内容，如果服务器没有返回了一个错误消息，那么几乎可以断定设置了 AllowOverride None 。
在访问文档时，如果收到服务器的出错消息，应该检查Apache的错误日志，可以知道.htaccess文件中哪些指令是不允许使用的，也可能会发现需要纠正的语法错误。

.htaccess工具

不会写的朋友,在这介绍一款很不错.htaccess的重定向—URL重写工具rewriting-tool

——————————————————————————–

htaccess语法教程

RewriteEngine On
RewriteCond %{HTTP_HOST} ^(www\.)?xxx\.com$
RewriteCond %{REQUEST_URI} !^/blog/
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /blog/$1

# 没有输入文件名的默认到到首页
RewriteCond %{HTTP_HOST} ^(www\.)?xxx\.com$
RewriteRule ^(/)?$ blog/index.php [L]
下面我开始解说一下上面的意思：

【RewriteEngine On】

表示重写引擎开，关闭off，作用就是方便的开启或关闭以下的语句，这样就不需要一条一条的注释语句了。

【RewriteCond %{HTTP_HOST} ^(www\.)?xxx\.com$】

这是重写条件，前面%{HTTP_HOST}表示当前访问的网址，只是指前缀部分，格式是www.xxx.com不包括“http://”和“/”，^表示 字符串开始，$表示字符串结尾，\.表示转义的. ，如果不转义也行，推荐转义，防止有些服务器不支持，?表示前面括号www\.出现0次或1次，这句规则的意思就是如果访问的网址是xxx.com或者 www.xxx.com就执行以下的语句，不符合就跳过。

【RewriteCond %{REQUEST_URI} !^/blog/】

也是重写条件，%{REQUEST_URI}表示访问的相对地址，就是相对根目录的地址，就是域名/后面的成分，格式上包括最前面的“/”，!表示非，这句语句表示访问的地址不以/blog/开头，只是开头^，没有结尾$

【RewriteCond %{REQUEST_FILENAME} !-f】

【RewriteCond %{REQUEST_FILENAME} !-d】

这两句语句的意思是请求的文件或路径是不存在的，如果文件或路径存在将返回已经存在的文件或路径

【RewriteRule ^(.*)$ /blog/$1】

重写规则，最重要的部分，意思是当上面的RewriteCond条件都满足的时候，将会执行此重写规则，^(.*)$是一个正则表达的 匹配，匹配的是当前请求的URL，^(.*)$意思是匹配当前URL任意字符，.表示任意单个字符，*表示匹配0次或N次（N>0），后面 /blog/$1是重写成分，意思是将前面匹配的字符重写成/blog/$1，这个$1表示反向匹配，引用的是前面第一个圆括号的成分，即^(.*)$中 的.* ，其实这儿将会出现一个问题，后面讨论。

【RewriteCond %{HTTP_HOST} ^(www\.)?xxx\.com$】

【RewriteRule ^(/)?$ blog/index.php [L]】

这两句的意思是指请求的host地址是www.xxx.com是，如果地址的结尾只有0个或者1个“/”时，将会重写到子目录下的主页，我猜想这主要因为重写后的地址是不能自动寻找主页的，需要自己指定。

现在说说出现的问题，RewriteRule ^(.*)$ /blog/$1 前部分 ^(.*)$ 将会匹配当前请求的url。

例如：请求网址是http://www.xxx.com/a.html，到底是匹配整个http://www.xxx.com/a.html，还是只匹配/a.html即反斜杠后面的成分，还是只匹配a.html。

答案是：根据RewriteBase规则规定，如果rewritebase 为/，将会匹配a.html，不带前面的反斜杠，所以上条语句应该写成RewriteRule ^(.*)$ blog/$1（不带/），不过实际应用上带上前面的反斜杠，也可以用，可能带不带都行。现在问题出来了，如果不设置rewritebase 为/ ，将会匹配整个网址http://www.xxx.com/a.html，显然这是错误的，所以应该添加这条：RewiteBase /

还有一个问题是，不能保证每个人输入的网址都是小写的，如果输入大写的呢，linux系统是区分大小写的，所以应该在RewriteCond后添加[NC]忽略大小写的。

至此，完整的语句应该是：

RewriteEngine On
RewiteBase /
RewriteCond %{HTTP_HOST} ^(www\.)?xxx\.com$ [NC]
RewriteCond %{REQUEST_URI} !^/blog/
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ blog/$1

# 没有输入文件名的默认到到首页
RewriteCond %{HTTP_HOST} ^(www\.)?xxx\.com$ [NC]
RewriteRule ^(/)?$ blog/index.php [L]
如果后面还继续有语句的，就不应该加上最后的[L]，因为这是表示最后一条语句的意思。

防盗链的语句，同样需要添加RewiteBase /，如下：

RewriteEngine on
RewiteBase /
RewriteCond %{HTTP_REFERER} !^$ [NC]
RewriteCond %{HTTP_REFERER} !xxx.info [NC]
RewriteRule \.(jpg|gif|png|bmp|swf|jpeg)$ /error/daolian.gif [R,NC,L]
如果后面还继续有语句的，就不应该加上最后的[L]，/error/daolian.gif为别人盗链时显示的图片。

下面附上简单的语法规则和flags

【RewriteCond语法】

RewriteCond TestString CondPattern [flags]

rewritecond的其他用法：

“-d”(目录)

将TestString视为一个路径名并测试它是否为一个存在的目录。

“-f”(常规文件)

将TestString视为一个路径名并测试它是否为一个存在的常规文件。

“-s”(非空的常规文件)

将TestString视为一个路径名并测试它是否为一个存在的、尺寸大于0的常规文件。

“-l”(符号连接)

将TestString视为一个路径名并测试它是否为一个存在的符号连接。

“-x”(可执行)

将TestString视为一个路径名并测试它是否为一个存在的、具有可执行权限的文件。该权限由操作系统检测。

“-F”(对子请求存在的文件)

检查TestString是否为一个有效的文件，而且可以在服务器当前的访问控制配置下被访问。它使用一个内部子请求来做检查，由于会降低服务器的性能，所以请谨慎使用！

“-U”(对子请求存在的URL)

检查TestString是否为一个有效的URL，而且可以在服务器当前的访问控制配置下被访问。它使用一个内部子请求来做检查，由于会降低服务器的性能，所以请谨慎使用！

【RewriteRule语法：】

RewriteRule Pattern Substitution [flags]

【flags】

“chain|C”(链接下一规则)

此标记使当前规则与下一个规则相链接。它产生这样的效果：如果一个规则被匹配，则继续处理其后继规则，也就是这个标记不起作用；如果该规则不被匹配，则其后继规则将被跳过。比如，在一个目录级规则中执行一个外部重定向时，你可能需要删除”.www”(此处不应该出现”.www”)。

“cookie|CO=NAME:VAL:domain[:lifetime[:path]]”(设置cookie)

在客户端设置一个cookie。cookie的名称是NAME，值是VAL。domain是该cookie的域，比如”.apache.org”，可选的lifetime是cookie的有效期(分钟)，可选的path是cookie的路径。

“env|E=VAR:VAL”(设置环境变量)

此标记将环境变量VAR的值为VAL，VAL可以包含可扩展的正则表达式反向引用($N和%N)。此标记可以多次使用以设置多个变量。这些变量可以在其后许多情况下被间接引用，通常是在XSSI(<!–#echo var=”VAR”–>)或CGI($ENV{“VAR”})中，也可以在后继的RewriteCond指令的CondPattern参数中通过%{ENV:VAR}引用。使用它可以记住从URL中剥离的信息。

“forbidden|F”(强制禁止URL)

强制禁止当前URL，也就是立即反馈一个HTTP响应码403(被禁止的)。使用这个标记，可以链接若干个RewriteConds来有条件地阻塞某些URL。

“gone|G”(强制废弃URL)

强制当前URL为已废弃，也就是立即反馈一个HTTP响应码410(已废弃的)。使用这个标记，可以标明页面已经被废弃而不存在了。

“handler|H=Content-handler”(强制指定内容处理器)

强自制定目标文件的内容处理器为Content-handler。例如，用来模拟mod_alias模块的ScriptAlias指令，以强制映射文件夹内的所有文件都由”cgi-script”处理器处理。

“last|L”(结尾规则)

立即停止重写操作，并不再应用其他重写规则。它对应于Perl中的last命令或C语言中的break命令。这个标记用于阻止当前已被重写的URL被后继规则再次重写。例如，使用它可以重写根路径的URL(“/”)为实际存在的URL(比如：”/e/www/”)。

“next|N”(从头再来)

重新执行重写操作(从第一个规则重新开始)。此时再次进行处理的URL已经不是原始的URL了，而是经最后一个重写规则处理过的URL。它对应于Perl中的next命令或C语言中的continue命令。此标记可以重新开始重写操作(立即回到循环的开头)。但是要小心，不要制造死循环！

“nocase|NC”(忽略大小写)

它使Pattern忽略大小写，也就是在Pattern与当前URL匹配时，”A-Z”和”a-z”没有区别。

“noescape|NE”(在输出中不对URI进行转义)

此标记阻止mod_rewrite对重写结果应用常规的URI转义规则。 一般情况下，特殊字符(“%”, “$”, “;”等)会被转义为等值的十六进制编码(“%25′, “%24′, “%3B”等)。此标记可以阻止这样的转义，以允许百分号等符号出现在输出中，比如：

RewriteRule /foo/(.*) /bar?arg=P1\%3d$1 [R,NE]

可以使”/foo/zed转向到一个安全的请求”/bar?arg=P1=zed”。

“nosubreq|NS”(不对内部子请求进行处理)

在当前请求是一个内部子请求时，此标记强制重写引擎跳过该重写规则。比如，在mod_include试图搜索目录默认文件(index.xxx)时，Apache会在内部产生子请求。对于子请求，重写规则不一定有用，而且如果整个规则集都起作用，它甚至可能会引发错误。所以，可以用这个标记来排除某些规则。

使用原则：如果你为URL添加了CGI脚本前缀，以强制它们由CGI脚本处理，但对子请求处理的出错率(或者资源开销)很高，在这种情况下，可以使用这个标记。

“proxy|P”(强制为代理)

此标记使替换成分被内部地强制作为代理请求发送，并立即中断重写处理，然后把处理移交给mod_proxy模块。你必须确保此替换串是一个能够被mod_proxy处理的有效URI(比如以http://hostname开头)，否则将得到一个代理模块返回的错误。使用这个标记，可以把某些远程成分映射到本地服务器域名空间，从而增强了ProxyPass指令的功能。

注意：要使用这个功能，必须已经启用了mod_proxy模块。

“passthrough|PT”(移交给下一个处理器)

此标记强制重写引擎将内部request_rec结构中的uri字段设置为filename字段的值，这个小小的修改使得RewriteRule指令的输出能够被(从URI转换到文件名的)Alias, ScriptAlias, Redirect等指令进行后续处理[原文：This flag is just a hack to enable post-processing of the output of RewriteRule directives, using Alias, ScriptAlias, Redirect, and other directives from various URI-to-filename translators.]。举一个能说明其含义的例子： 如果要将/abc重写为/def， 然后再使用mod_alias将/def转换为/ghi，可以这样：

RewriteRule ^/abc(.*) /def$1 [PT]

Alias /def /ghi

如果省略了PT标记，虽然将uri=/abc/…重写为filename=/def/…的部分运作正常，但是后续的mod_alias在试图将URI转换到文件名时会遭遇失效。

注意：如果需要混合使用多个将URI转换到文件名的模块时，就必须使用这个标记。。此处混合使用mod_alias和mod_rewrite就是个典型的例子。

“qsappend|QSA”(追加查询字符串)

此标记强制重写引擎在已有的替换字符串中追加一个查询字符串，而不是简单的替换。如果需要通过重写规则在请求串中增加信息，就可以使用这个标记。

“redirect|R [=code]“(强制重定向)

若Substitution以http://thishost[:thisport]/(使新的URL成为一个URI)开头，可以强制性执行一个外部重定向。如果没有指定code，则产生一个HTTP响应码302(临时性移动)。如果需要使用在300-400范围内的其他响应代码，只需在此指定即可(或使用下列符号名称之一：temp(默认), permanent, seeother)。使用它可以把规范化的URL反馈给客户端，如将”/~”重写为”/u/”，或始终对/u/user加上斜杠，等等。

注意：在使用这个标记时，必须确保该替换字段是一个有效的URL。否则，它会指向一个无效的位置！并且要记住，此标记本身只是对URL加上http://thishost[:thisport]/前缀，重写操作仍然会继续进行。通常，你还会希望停止重写操作而立即重定向，那么就还需要使用”L’标记。

“skip|S=num”(跳过后继规则)

此标记强制重写引擎跳过当前匹配规则之后的num个规则。它可以模拟if-then-else结构：最后一个规则是then从句，而被跳过的skip=N个规则是else从句。注意：它和”chain|C”标记是不同的！

“type|T=MIME-type”(强制MIME类型)

强制目标文件的MIME类型为MIME-type，可以用来基于某些特定条件强制设置内容类型。比如，下面的指令可以让.php文件在以.phps扩展名调用的情况下由mod_php按照PHP源代码的MIME类型(application/x-httpd-php-source)显示：

RewriteRule ^(.+\.php)s$ $1 [T=application/x-httpd-php-source]

.htaccess实例

http://cloudbbs.org/forum.php?mod=viewthread&tid=7455&page=1&extra=#pid41053

http://www.chinaz.com/web/2010/0415/111514.shtml

参考：http://baike.baidu.com/view/91163.htm

http://hi.baidu.com/wojiubaibudu/item/4b3513c74a8fe47aced4f817

.htaccess rewrite 规则详细说明
 

来源网址： http://www.cnphp.info/htaccess-rewrite.html

作者: freemouse 日期 2010年07月22日 | 可以转载, 但必须以超链接形式标明文章原始出处和作者信息及版权声明

网址: http://www.cnphp.info/htaccess-rewrite.html

用Apache虚拟主机的朋友很多，apache提供的.htaccess模块可以为每个虚拟主机设定rewrite规则，这对网站SEO优化相当有用，同时也改善了用户体验。国内的虚拟机一般不提供.htaccess功能（据我所知，discuz的主机好像提供此功能），而在国外主机中，.htaccess功能似乎是标配，笔者的Blog架在MT上，支持.htaccess，每次看到一堆别人写好了的.htaccess设置，很多命令都不甚了了，查看、修改起来很不方便，痛定思痛，潜心学习一下，知其所以然嘛～

学习前提：（不会的朋友要学习一下，才能更好的理解下面的文字呢）

Linux基础（不会也没事啦，写个.htaccess没必要大费周折啦，推荐：鸟哥私房菜linux基础）
正则表达式（Rewrite规则建立在正则的基础之上，推荐：正则表达式30分钟入门教程）
rewrite的语法格式：

RewriteEngine On #要想rewrite起作用，必须要写上哦
RewriteBase url-path #设定基准目录，例如希望对根目录下的文件rewrtie，就是”/”
RewriteCond test-string condPattern #写在RewriteRule之前，可以有一或N条，用于测试rewrite的匹配条件，具体怎么写，后面会详细说到。
RewriteRule Pattern Substitution #规则
RewriteEngine On|Off
RewriteEngine 用于开启或停用rewrite功能。

rewrite configurations 不会自动继承，因此你得给每个你想用 rewrite功能的虚拟主机目录中加上这个指令。

RewriteBase URL-path
RewriteBase用于设定重写的基准URL。在下文中，你可以看见RewriteRule可以用于目录级的配置文件中 (.htaccess)并在局部范围内起作用，即规则实际处理的只是剥离了本地路径前缀的一部分。处理结束后，这个路径会被自动地附着回去。默认值 是”RewriteBase physical-directory-path”。

在对一个新的URL进行替换时，此模块必须把这个URL重新注入到服务器处理中。为此，它必须知道其对应的URL前缀或者说URL基准。通常，此前缀就是 对应的文件路径。但是，大多数网站URL不是直接对应于其物理文件路径的，因而一般不能做这样的假定! 所以在这种情况下，就必须用RewriteBase指令来指定正确的URL前缀。

如果你的网站服务器URL不是与物理文件路径直接对应的，而又需要使用RewriteBase指令，则必须在每个对应的.htaccess文件中指定 RewriteRule 。

RewriteCond TestString CondPattern [flags]
RewriteCond指令定义了一个规则的条件，即，在一个RewriteRule指令之前有一个或多个RewriteCond指令。 条件之后的重写规则仅在当前URI与pattern匹配并且符合这些条件的时候才会起作用。

TestString是一个纯文本的字符串，但是还可以包含下列可扩展的成分：

RewriteRule反向引用: 引用方法是 $N  (0 <= N <= 9) 引用当前(带有若干RewriteCond指令的)RewriteRule中的 与pattern匹配的分组成分(圆括号!)。
RewriteCond反向引用: 引用方法是 %N  (1 <= N <= 9) 引用当前若干RewriteCond条件中最后符合的条件中的分组成分(圆括号!)。
RewriteMap 扩展: 引用方法是 ${mapname:key|default}
服务器变量: 引用方法是 %{ NAME_OF_VARIABLE }  这个是我们最常使用到的功能
NAME_OF_VARIABLE具体数值见下表:

HTTP headers:

connection & request:

HTTP_USER_AGENT

HTTP_REFERER

HTTP_COOKIE

HTTP_FORWARDED

HTTP_HOST

HTTP_PROXY_CONNECTION

HTTP_ACCEPT

REMOTE_ADDR

REMOTE_HOST

REMOTE_USER

REMOTE_IDENT

REQUEST_METHOD

SCRIPT_FILENAME

PATH_INFO

QUERY_STRING

AUTH_TYPE

server internals:

system stuff:

specials:

DOCUMENT_ROOT

SERVER_ADMIN

SERVER_NAME

SERVER_ADDR

SERVER_PORT

SERVER_PROTOCOL

SERVER_SOFTWARE

TIME_YEAR

TIME_MON

TIME_DAY

TIME_HOUR

TIME_MIN

TIME_SEC

TIME_WDAY

TIME

API_VERSION

THE_REQUEST

REQUEST_URI

REQUEST_FILENAME

IS_SUBREQ

这些都对应于类似命名的HTTP MIME头、Apache服务器的C变量以及Unix系统中的 struct tm字段，大多数都在其他的手册或者CGI规范中有所讲述。 而其中为mod_rewrite所特有的变量有:

IS_SUBREQ

如果正在处理的请求是一个子请求，它包含字符串”true”，否则就是”false”。 模块为了解析URI中的附加文件，有可能会产生子请求。

API_VERSION

这是正在使用的httpd中(服务器和模块之间内部接口)的Apache模块API的版本， 其定义位于include/ap_mmn.h中。此模块版本对应于正在使用的Apache的版本 (比如，在Apache 1.3.14的发行版中，这个值是19990320:10)。 通常，对它感兴趣的是模块的作者。

THE_REQUEST

这是由浏览器发送给服务器的完整的HTTP请求行。(比如, “GET /index.html HTTP/1.1″). 它不包含任何浏览器发送的附加头信息。

REQUEST_URI

这是在HTTP请求行中所请求的资源。(比如上述例子中的”/index.html”.)

REQUEST_FILENAME

这是与请求相匹配的完整的本地文件系统的文件路径名或描述.

CondPattern是条件pattern, 即, 一个应用于当前实例TestString的正则表达式, 即, TestString将会被计算然后与CondPattern匹配.

注意：CondPattern是一个兼容perl的正则表达式， 但是还有若干补充：

可以在pattern串中使用’
1	
!
‘ 字符(惊叹号)来实现匹配的反转。

RewriteOptions Options
1	
RewriteOptions
指令为当前服务器级和目录级的配置设置一些选项。 Option可以是下列值之一：

1	
inherit
此值强制当前配置可以继承其父配置。 在虚拟主机级配置中，它意味着主服务器的映射表、条件和规则可以被继承。 在目录级配置中，它意味着其父目录的
1	
.htaccess
中的条件和规则可以被继承。

1	
MaxRedirects=<var>number</var>
为了避免目录级
1	
RewriteRule
的无休止的内部重定向， 在此类重定向和500内部服务器错误次数达到一个最大值的时候，

1	
mod_rewrite
会停止对此请求的处理。 如果你确实需要对每个请求允许大于10次的内部重定向，可以增大这个值。

RewriteRule Pattern Substitution [flags]
1	
RewriteRule
指令是重写引擎的根本。此指令可以多次使用。 每个指令定义一个简单的重写规则。这些规则的定义顺序尤为重要, 因为，在运行时刻，规则是按这个顺序逐一生效的.

Pattern是一个作用于当前URL的兼容perl的正则表达式。

此外，还可以使用否字符(‘

1	
!
‘)的pattern前缀，以实现pattern的反转。但是，需要注意的是使用否字符以反转pattern时，pattern中不能使用分组的通配成分；即$N。

重写规则中的Substitution是， 当原始URL与Pattern相匹配时，用以替代(或替换)的字符串。除了纯文本，还可以使用

1	
$N
反向引用RewriteRule的pattern

1	
%N
反向引用最后匹配的RewriteCond pattern

规则条件测试字符串中(
1	
%{VARNAME}
)的服务器变量

映射函数调用(
1	
${mapname:key|default})
下面给出几个完整的例子供各位参考：
一、防盗链功能

只这四行就实现了防盗链是不是很神奇^_^，编写起来是不是又觉得复杂。

RewriteEngine On

RewriteCond %{HTTP_REFERER} !^http://(.+.)?mysite.com/ [NC]

RewriteCond %{HTTP_REFERER} !^$

RewriteRule .*.(jpe?g|gif|bmp|png)$ /images/nohotlink.jpg [L]

二、网址规范化

这个是把所有二级域名都重定向到www.yourdomain.com的例子，现在看来是不是很简单了？

Options +FollowSymLinks

rewriteEngine on

rewriteCond %{http_host} ^yourdomain.com [NC]

rewriteRule ^(.*)$ http://www.yourdomain.com/$1 [R=301,L]

三、临时错误页面

当你的网站在升级、修改的时候，你最好让访客转到指定的页面，而不是没做完的页面或者是错误页。

RewriteEngine on

RewriteCond %{REQUEST_URI} !/maintenance.html$

RewriteCond %{REMOTE_ADDR} !^123.123.123.123

RewriteRule $ /error.html [R=302,L]

四、重定向RSS地址到FeedSky

除了可以更改模板里的RSS地址外，.htaccess也能实现RSS地址的更改，并更加方便。

RewriteEngine on

RewriteCond %{HTTP_USER_AGENT} !FeedSky [NC]

RewriteCond %{HTTP_USER_AGENT} !FeedValidator [NC]

RewriteRule ^feed/?([_0-9a-z-]+)?/?$ http://feed.feedsky.com/yours

=========================================================================================

附录：flags

‘redirect|R [=code]‘ (强制重定向 redirect)
以http://thishost[:thisport]/(使新的URL成为一个URI) 为前缀的Substitution可以强制性执行一个外部重定向。 如果code没有指定，则产生一个HTTP响应代码302(临时性移动)。 如果需要使用在300-400范围内的其他响应代码，只需在此指定这个数值即可， 另外，还可以使用下列符号名称之一: temp (默认的), permanent, seeother. 用它可以把规范化的URL反馈给客户端，如, 重写“/~”为 “/u/”，或对/u/user加上斜杠，等等。 注意: 在使用这个标记时，必须确保该替换字段是一个有效的URL! 否则，它会指向一个无效的位置! 并且要记住，此标记本身只是对URL加上 http://thishost[:thisport]/的前缀，重写操作仍然会继续。 通常，你会希望停止重写操作而立即重定向，则还需要使用’L’标记.

‘forbidden|F’ (强制URL为被禁止的 forbidden)
强制当前URL为被禁止的，即，立即反馈一个HTTP响应代码403(被禁止的)。 使用这个标记，可以链接若干RewriteConds以有条件地阻塞某些URL。

‘gone|G’ (强制URL为已废弃的 gone)
强制当前URL为已废弃的，即，立即反馈一个HTTP响应代码410(已废弃的)。 使用这个标记，可以标明页面已经被废弃而不存在了.

‘proxy|P’ (强制为代理 proxy)
此标记使替换成分被内部地强制为代理请求，并立即(即， 重写规则处理立即中断)把处理移交给代理模块。 你必须确保此替换串是一个有效的(比如常见的以 http://hostname开头的)能够为Apache代理模块所处理的URI。 使用这个标记，可以把某些远程成分映射到本地服务器名称空间， 从而增强了ProxyPass指令的功能。 注意: 要使用这个功能，代理模块必须编译在Apache服务器中。 如果你不能确定，可以检查“httpd -l”的输出中是否有mod_proxy.c。 如果有，则mod_rewrite可以使用这个功能； 如果没有，则必须启用mod_proxy并重新编译“httpd”程序。

‘last|L’ (最后一个规则 last)
立即停止重写操作，并不再应用其他重写规则。 它对应于Perl中的last命令或C语言中的break命令。 这个标记可以阻止当前已被重写的URL为其后继的规则所重写。 举例，使用它可以重写根路径的URL(‘/’)为实际存在的URL, 比如, ‘/e/www/’.

‘next|N’ (重新执行 next round)
重新执行重写操作(从第一个规则重新开始). 这时再次进行处理的URL已经不是原始的URL了，而是经最后一个重写规则处理的URL。 它对应于Perl中的next命令或C语言中的continue命令。 此标记可以重新开始重写操作，即, 立即回到循环的头部。 但是要小心，不要制造死循环!

‘chain|C’ (与下一个规则相链接 chained)
此标记使当前规则与下一个(其本身又可以与其后继规则相链接的， 并可以如此反复的)规则相链接。 它产生这样一个效果: 如果一个规则被匹配，通常会继续处理其后继规则， 即，这个标记不起作用；如果规则不能被匹配， 则其后继的链接的规则会被忽略。比如，在执行一个外部重定向时， 对一个目录级规则集，你可能需要删除“.www” (此处不应该出现“.www”的)。

‘type|T=MIME-type’ (强制MIME类型 type)
强制目标文件的MIME类型为MIME-type。 比如，它可以用于模拟mod_alias中的ScriptAlias指令， 以内部地强制被映射目录中的所有文件的MIME类型为“application/x-httpd-cgi”.

‘nosubreq|NS’ (仅用于不对内部子请求进行处理 no internal sub-request)
在当前请求是一个内部子请求时，此标记强制重写引擎跳过该重写规则。 比如，在mod_include试图搜索可能的目录默认文件(index.xxx)时， Apache会内部地产生子请求。对子请求，它不一定有用的，而且如果整个规则集都起作用， 它甚至可能会引发错误。所以，可以用这个标记来排除某些规则。 根据你的需要遵循以下原则: 如果你使用了有CGI脚本的URL前缀，以强制它们由CGI脚本处理， 而对子请求处理的出错率(或者开销)很高，在这种情况下，可以使用这个标记。

‘nocase|NC’ (忽略大小写 no case)
它使Pattern忽略大小写，即, 在Pattern与当前URL匹配时，’A-Z’ 和’a-z’没有区别。

‘qsappend|QSA’ (追加请求串 query string append)
此标记强制重写引擎在已有的替换串中追加一个请求串，而不是简单的替换。 如果需要通过重写规则在请求串中增加信息，就可以使用这个标记。

‘noescape|NE’ (在输出中不对URI作转义 no URI escaping)
此标记阻止mod_rewrite对重写结果应用常规的URI转义规则。 一般情况下，特殊字符(如’%’, ‘$’, ‘;’等)会被转义为等值的十六进制编码。 此标记可以阻止这样的转义，以允许百分号等符号出现在输出中，如： RewriteRule /foo/(.*) /bar?arg=P1\%3d$1 [R,NE]

可以使’/foo/zed’转向到一个安全的请求’/bar?arg=P1=zed’.

‘passthrough|PT’ (移交给下一个处理器 pass through)
此标记强制重写引擎将内部结构request_rec中的uri字段设置为 filename字段的值，它只是一个小修改，使之能对来自其他URI到文件名翻译器的 Alias，ScriptAlias, Redirect 等指令的输出进行后续处理。举一个能说明其含义的例子： 如果要通过mod_rewrite的重写引擎重写/abc为/def， 然后通过mod_alias使/def转变为/ghi，可以这样: RewriteRule ^/abc(.*) /def$1 [PT]

Alias /def /ghi

如果省略了PT标记，虽然mod_rewrite运作正常， 即, 作为一个使用API的URI到文件名翻译器， 它可以重写uri=/abc/…为filename=/def/…， 但是，后续的mod_alias在试图作URI到文件名的翻译时，则会失效。

注意: 如果需要混合使用不同的包含URI到文件名翻译器的模块时， 就必须使用这个标记。混合使用mod_alias和mod_rewrite就是个典型的例子。

For Apache hackers

如果当前Apache API除了URI到文件名hook之外，还有一个文件名到文件名的hook， 就不需要这个标记了! 但是，如果没有这样一个hook，则此标记是唯一的解决方案。 Apache Group讨论过这个问题，并在Apache 2.0 版本中会增加这样一个hook。

’skip|S=num’ (跳过后继的规则 skip)
此标记强制重写引擎跳过当前匹配规则后继的num个规则。 它可以实现一个伪if-then-else的构造: 最后一个规则是then从句，而被跳过的skip=N个规则是else从句. (它和’chain|C’标记是不同的!)

‘env|E=VAR:VAL’ (设置环境变量 environment variable)
此标记使环境变量VAR的值为VAL, VAL可以包含可扩展的反向引用的正则表达式$N和%N。 此标记可以多次使用以设置多个变量。 这些变量可以在其后许多情况下被间接引用，但通常是在XSSI (via or CGI (如 $ENV{‘VAR’})中， 也可以在后继的RewriteCond指令的pattern中通过%{ENV:VAR}作引用。 使用它可以从URL中剥离并记住一些信息。

‘cookie|CO=NAME:VAL:domain[:lifetime[:path]]’ (设置cookie)
它在客户端浏览器上设置一个cookie。 cookie的名称是NAME，其值是VAL。 domain字段是该cookie的域，比如’.apache.org’, 可选的lifetime是cookie生命期的分钟数， 可选的path是cookie的路径。

深入阅读：http://oss.org.cn/man/newsoft/ApacheManual/mod/mod_rewrite.html

全面理解.htaccess语法中RewriteCond和RewriteRule意义
 

来源网址： http://blog.sina.com.cn/s/blog_7048e38101017xdx.html

(2012-08-13 10:38:44)

关于.htaccess伪静态的使用，章郎虫一直没有好好想过。以前一直是在网上找现成的，然后修改下网址实现重定向。今天我专门找资料看了下RewriteCond和RewriteRule的意思及使用方法。然后回过头看《网站地址更改之htaccess和php的301重定向》这篇文章，终于有些理解。现在不用一直找现成的代码，也可以自己写一些规则实现重定向了。下面就简单的介绍下他们的用法。

RewriteCond的语法

RewriteCond TestString CondPattern [Flags]

其中的TestString是指一个文本格式的条件，例子中用的是环境变量名HTTP_HOST所包含的内容（Name= Value），这是一个map（键值对）格式的数据类型。

CondPattern是条件参数，这儿以第一个例子为例，就是abc.com。

Flags标识是是第三个参数，可以用来紧跟下一个条件，这儿用OR表示或者，如果没有[Flags]，则用隐含的AND，表示并且。其它的还可以NC等等，表示忽略大小写

RewriteCond就像我们程序中的if语句一样，表示如果符合某个或某几个条件则执行RewriteCond下面紧邻的RewriteRule语句，这就是RewriteCond最原始、基础的功能，为了方便理解，下面来看看几个例子。

RewriteEngine on

RewriteCond %{HTTP_USER_AGENT} ^Mozilla/5.0.*

RewriteRule index.php index.m.php

RewriteCond %{HTTP_USER_AGENT} ^Lynx.*

RewriteRule index.php index.L.php

RewriteRule index.php index.b.php

上面语句的作用是当你是用FF浏览器访问index.php这个文件的时候，会自动让你访问到index.m.php这个文件，当你是用一些移动终端访问 的 时候，会让你对index.php这个文件的访问实际访问的是index.L.php去，如果你是用其它的浏览器访问的时候，会让你跳到 index.b.php。

RewriteRule的语法

RewriteRule Pattern Substitution [Flags]

其中的Pattern就是参数，一般为一些文件的扩展名，Substitution是用来替换前面用的，这儿的Flags，常用的R表示 redirect（强制重定向），F表示forbidden（禁止访问），L表示last（最后），通常当你希望停止重写操作而立即重定向时，可用它。

.htaccess中用到的正则

元字符^（和数字6在同一个键位上的符号）和$都匹配一个位置，这和\b有点类似。

^匹配你要用来查找的字符串的开头

$匹配结尾。

比如一个网站如果要求你填写的QQ号必须为5位到12位数字时，可以使用：^\d{5,12}$。

如果你对正则表达式不是很明白，可以看下正则表达式的教程。

Source from: http://www.hellonet8.com/897.html

 

URL重写 htaccess文件写法的10个技巧
 

来源网址： http://blog.sina.com.cn/s/blog_7069146d01015ikf.html

(2012-07-26 03:25:44)

“.htaccess”文件往往被网页设计师们忽略。假如你还不知道什么是htaccess的话，你可以去查一下wikipedia。它是目录级别的配置文件，有常用的网页服务器支持这种配置，例如Apache。下面我将列出10条有用的.htaccess配置技巧。

1. 反盗链

那些盗用了你的内容，还不愿意自己存储图片的网站是无耻的。你可以通过以下配置来放置别人盗用你的图片：

RewriteBase /

RewriteCond %{HTTP_REFERER} !^$

RewriteCond %{HTTP_REFERER} !^http://(www.)?yoursite.com/.*$ [NC]

RewriteRule .(gif|jpg|swf|flv|png)$ /feed/ [R=302,L]

2. 防止目录浏览

有时候目录浏览是有用的，但大部分情况会有安全问题。为了让你的网站更安全，你可以通过htaccess文件来禁用这个功能：

Options All -Indexes

3. SEO友好的301永久重定向

这一招是我常用的。每次我更改网站URL结构的时候，我都会做301重定向：

Redirect 301 http://www.yoursite.com/article.html http://www.yoursite.com/archives/article 4. 显示个性化的 404 错误页面

当用户访问了一个不存在的页面的时候，网页服务器会显示“404 file not found”错误。有很多CMS可以让你设置自定义的错误页面，但最简单的方法是更改htaccess：

ErrorDocument 404 /404.html

5. 设置目录的默认页面

假如你需要为不同的目录设置不同的默认页面，你可以很容易的通过 .htaccess 实现：

DirectoryIndex about.html

6. 基于referer来限制网站访问

站长通常不会限制网站访问，但是当你发现有一些网站尽给你带来垃圾流量的话，你就应该屏蔽他们：

<IfModule mod_rewrite.c>

RewriteEngine on  RewriteCond %{HTTP_REFERER} spamteam.com [NC,OR]

RewriteCond %{HTTP_REFERER} trollteam.com [NC,OR]

RewriteRule .* – [F]

</ifModule>

7. 限制PHP上传文件大小

这招在共享空间的服务器上很有用，可以让我的用户上传更大的文件。第一个是设置最大的上传文件大小，第二个是设置最大的POST请求大小，第三个PHP脚本最长的执行时间，最后一个是脚本解析上传文件的最长时间：

php_value upload_max_filesize 20M

php_value post_max_size 20M

php_value max_execution_time 200

php_value max_input_time 200

8. 压缩文件

你可以通过压缩文件来减少网络流量，也页面装载时间：

AddOutputFilterByType DEFLATE text/plain

AddOutputFilterByType DEFLATE text/html

AddOutputFilterByType DEFLATE text/xml

AddOutputFilterByType DEFLATE text/css

AddOutputFilterByType DEFLATE application/xml

AddOutputFilterByType DEFLATE application/xhtml+xml

AddOutputFilterByType DEFLATE application/rss+xml

AddOutputFilterByType DEFLATE application/javascript

AddOutputFilterByType DEFLATE application/x-javascript

9. 缓存文件

这一点还需要解释吗？

<FilesMatch “.(flv|gif|jpg|jpeg|png|ico|swf|js|css|pdf)$”>

Header set Cache-Control “max-age=2592000〃

</FilesMatch>

10. 添加尾部的反斜杠

我并不确定，但是很多文章，很多人都说添加尾部反斜杠有益于SEO：

<IfModule mod_rewrite.c>

RewriteCond %{REQUEST_URI} /+[^\.]+$

RewriteRule ^(.+[^/])$ %{REQUEST_URI}/ [R=301,L]

</IfModule>

====================

引用：http://www.c658.com/658/html/xxlm/itxxl/882.html

.htaccess基本语法和应用
.htaccess是Apache服务器的一个非常强大的分布式配置文件。

正确的理解和使用.htaccess文件，可以帮助我们优化自己的服务器或者虚拟主机。

如何启用htaccess
以windows为例，进入apache/conf目录，找到httpd.conf文件，去掉

LoadModule rewrite_module modules/mod_rewrite.so

前面的#，然后设置目录属性AllowOverride All，重启apache即可

下面是一个典型的htaccess文件

           # 开启URL重写
RewriteEngine on
# URL重写的作用域
# RewriteBase /path/to/url
# 满足怎样的条件
RewriteCond %{HTTP_HOST} !^www\.example\.com$ [NC]
# 应用怎样的规则
RewriteRule .? http://www.example.com%{REQUEST_URI} [R=301,L]
来看看RewriteCond，首先有一个%，因为{HTTP_HOST}是一个apache变量，需要用%来指示。从!开始就是匹配的条件，支持 正则。!表示不等于，这句话的意思就是：如果HTTP_HOST不是www.example.com。后面的[NC](no case)表示忽略大小写，常见的还有

[L](last)：终止一系列的RewriteCond和RewriteRule
[R](redirect)：触发一个显示的跳转，也可以指定跳转类型，如[R=301]
[F](forbidden)：禁止查看特定文件，apache会触发403错误
图片防盗链

           RewriteCond %{HTTP_REFERER} !^$
RewriteCond %{HTTP_REFERER} !^http://(www\.)?example\.com/ [NC]
RewriteRule \.(gif|jpg|png)$ - [F]
由于是基于HTTP_REFERER的验证，所以只能防止一般的图片盗链，因为HTTP_REFERER是比较容易伪造的

自定义404错误页面

如果用户输入了一个不存在的url，那么就显示自定义的错误页面

           ErrorDocument 404 /404.html
# 其他同理
ErrorDocument 500 /500.html
处理移动过的文件

           Redirect 301 /old.html http://yoursite.com/new.html
# 也可以是下面这样
RewriteRule /old.html http://yoursite.com/new.html [R=301,L]
# 如果想隐式跳转(URL地址不变，但实际上内容是其他URL的)，就使用下面的
RewriteRule /old.html http://yoursite.com/new.html [L]
对于RewriteRule还有好多文章可以做，比如

           # 把html后缀的url链接到php文件
# $1指代的是前面第1个用括号括起来的内容
RewriteRule ^/?([a-z/]+)\.html$ $1.php [L]
# 或者把旧文件夹的内容链接到新文件夹
RewriteRule ^/?old_directory/([a-z/.]+)$ new_directory/$1 [R=301,L]
# 隐藏文件名
RewriteRule ^/?([a-z]+)$ $1.php [L]
禁止显示目录列表
如果目录里没有index文件，又没有对该目录做过特别的处理，尤其是windows主机，那么该目录里的内容就会显示出来，这时可以在根目录创建 一个.htaccess文件，然后写上

           Options -Indexes
# 就这么一句就搞定了
阻止/允许特定IP/IP段

           # 禁止所有IP，除了指定的
order deny,allow
deny from all
# 如果想允许IP段，如123.123.123.0 ~ 123.123.123.255，则
# allow from 123.123.123.
allow from 123.123.123.123

ErrorDocument 403 /page.html

<Files page.html>
allow from all
</Files>

#如果想禁止特定IP
deny from 123.123.123.123
添加MIME类型

           AddType video/x-flv .flv
# 如果设置类型为 application/octet-stream 将提示下载
AddType application/octet-stream .pdf
用.htaccess文件实现网站404错误
 

来源网址： http://www.os1010.com/archives/618

作者：admin  发表于：2012年06月11日 09:25  分类：SEO技术     字体： 小 中 大

定义404错误 页对网站SEO的作用还是很大的，404 错误意味着链接指向的网页不存在，即原始网页的URL失效，这种情况经常会发生，很难避免，当Web 服务器接到类似请求时，会返回一个404 状态码，告诉浏览器要请求的资源并不存在。但是，Web服务器默认的404错误页面，十分呆板，而且对SEO是不利，对于网站流量也是很大的损失。

现在大多数主机都提供设置404页面的接口，这样的无论是国内主机还是国外主机都很好设置，不过仍然有不少主机不提供设置页面，这样的多是国内主机和一些免费主机，本文主要是针对这些主机，而且是针对PHP主机。

1. Apache下设置404错误页面（一般是Linux主机）

(1)           在.htaccess 文件(如果没有则新建一个)中加入如下内容：ErrorDocument 404 /404.html，将.htaccess文件上传到网站根目录

注：也可以使用这样的命令

ErrorDocument 404 http://www.iewb.net/404.htm

ErrorDocument 500 http://www.iewb.net/500.htm

(2)           制作一个404页面，随便您设计，命名为404.html，同样上传到网站根目录。如果您还想设置500页面，还可以在.htaccess命令里加上ErrorDocument 404 /500.html 并制作一个500页面传到网站根目录

网友不必检验本站的404页面了，因为本站用的是godaddy免费的空间，404页面会有广告。

本文由新未来博客（www.os1010.com）整理，转载请注明!

本文固定链接: http://www.os1010.com/archives/618 | WordPress主机|香港主机空间|香港高速主机|新未来博客

由浅入深剖析.htaccess
 

来源网址： http://blog.csdn.net/cdefg198/article/details/6645759

2011-07-29 23:36 210人阅读 评论(0) 收藏 举报

1、.htaccess文件使用前提
.htaccess的主要作用就是实现url改写，也就是当浏览器通过url访问到服务器某个文件夹时，作为主人，我们可以来接待这个url，具体地怎样接待它，就是此文件的作用。所有的访问都是通过URL实现，所以.htaccess的作用非同小可。正因为此，所以一般地网站通过设置.htaccess，通过一个十分友好的url吸引用户进来，然后用.htaccess把用户带到需要访问的位置。

要想使用这个强大功能，就得开启apache里面的重写模块。

前面的文章中曾经讲到过windows和ubuntu开启 rewrite模块使用.htaccess 。

其实开启模块大体的步骤都是一样的，无论是Windows和linux。

2、.htaccess基本语法介绍
开启重写引擎 ：RewriteEngine on

设置重写的根目录：RewriteBase /     — 说明 ：因为定义了这个文件夹，所以对应的替换就有了一个参照。

匹配所有符合条件的请求：RewriteCond       — 说明：RewriteCond 定义了一系列规则条件，这个指令可以有一条或者多条，只有用户拿来的url符合这些条件之后，我们的.htaccess才开始接待，否则用户就直接自己去访问所需要的目录了。

举个例子，为了能让搜索引擎更多地抓取我们的网页而避免重复抓，我们通常把没有www的域名重定向到www.XXX.com，如下就实现了这个功能：

RewriteEngine On

RewriteCond %{HTTP_HOST}  ^nbphp\.com$ [NC]

RewriteRule ^(.*)$  http://www.nbphp.com/$1 [R=301,L]

上例便把nbphp.com 重定向到www.nbphp.com

%{HTTP_HOST} 是指取得用户访问的URL的主域名  然后空格后面是一个正则表达式匹配，意识就是说是否是 nbphp.com 。

如果用户访问使用的URL满足所有列出的RewriteCond 提出的条件，那么进行下一步RewriteRule 即开始进行引导，这才开始实现.htaccess文件的重要功能。

同样，前面是正则表达式，用户分析用户的除了主域名nbphp.com之外的URL ,^(.*)$的意思就是所有的内容。 然后空格后面写的是我们引导用户访问的目录，我们带着他走到新的一个域名上。$1 指的是前面括号里匹配url所得到的内容。

这样就是一个完整的小例子。关于RewriteCond里 如何调用url的某个部分，我们可以参考这篇文章（Apache的Mod_rewrite学习 (RewriteCond重写规则的条件)；

3、现学现用，学习正则表达式。
推荐一个经典的教程： 正则表达式30分钟入门教程

这个教程的确很简单，看完基本上写一些简单的正则就没有问题了。正则是一个需要长期使用的工具，隔段时间不用会忘记，所以我每次都看一遍这个教程。其实学过之后重要的就是一点内容。我简单罗列了如下：

.  换行符以外的所有字符

\w匹配字母或数字或下划线或汉字

\s匹配任意的空白符

\d匹配数字

\b匹配单词的开始或结束

^匹配字符串的开始

$匹配字符串的结束

*重复零次或更多次

*重复零次或更多次

+重复一次或更多次

?重复零次或一次

{n}重复n次

{n,}重复n次或更多次

{n,m}重复n到m次

应用替换时，前面第一个（）中匹配的内容后面就用$1引用，第二个（）中匹配的就用$2应用……

推荐一个实用的正则在线测试网站 http://www.regextester.com/

我们来分析一下 discuz7.0 搜索引擎优化 htaccess 里面的重写。

RewriteRule ^forum-([0-9]+)-([0-9]+)\.html$  forumdisplay.php?fid=$1&page=$2

首先加入用户通过 nbphp.com/forum-2-3.html 访问discuz论坛，那么先通过.htaccess过滤，看看是否需要.htaccess引导一下用户，如果满足列出的一系列RewriteCond的条件那么就进行重写，discuz的没有列出RewriteCond 所以应该全部都进行重写。所以开始进行转写，forum-2-3.html 这个正好符合 列出的^forum-([0-9]+)-([0-9]+)\.html$ 正则表达式。并且 $1 为 2  ，$2为3 ，所以代入后面，即 forumdisplay.php?fid=2&page=3 加上前面的RewriteBase 指定的文件目录，那么就带他到制定目录的forumdisplay.php?fid=2&page=3 。

4、常见的.htaccess应用举例（部分例子引自四个例子实战讲解.htaccess文件rewrite规则）
4.1防止盗链，如果来得要访问jpe jpg bmp png结尾的url 用户不是来自我们的网站，那么让他看一张我们网站的展示图片。
RewriteEngine On

RewriteCond %{HTTP_REFERER} !^http://(.+.)?mysite.com/ [NC]

RewriteCond %{HTTP_REFERER} !^$

RewriteRule .*.(jpe?g|gif|bmp|png)$ /images/nohotlink.jpg [L]

4.2 网站升级的时候，只有特定IP才能访问，其他的用户将看到一个升级页面
RewriteEngine on

RewriteCond %{REQUEST_URI} !/upgrade.html$

RewriteCond %{REMOTE_HOST} !^24\.121\.202\.30

RewriteRule $ http://www.nbphp.com/upgrade.html [R=302,L]

4.3把老的域名转向新域名
# redirect from old domain to new domain

RewriteEngine On

RewriteRule ^(.*)$http://www.yourdomain.com/$1[R=301,L]

5、一些其他功能
5.1 引出错误文档的目录
ErrorDocument 400 /errors/badrequest.html

ErrorDocument 404   http://yoursite/errors/notfound.html

ErrorDocument 401 “Authorization Required

5.2 Blocking users by IP 根据IP阻止用户访问
order allow,deny

deny from 123.45.6.7

deny from 12.34.5. (整个C类地址)

allow from all

5.3 防止目录浏览
# disable directory browsing

Options All -Indexes

5.4设置默认首页
# serve alternate default index page

DirectoryIndex about.html

5.5 把一些老的链接转到新的链接上——搜索引擎优化SEO
Redirect 301 /d/file.htmlhttp://www.htaccesselite.com/r/file.html

5.6为服务器管理员设置电子邮件。
ServerSignature EMail

SetEnv SERVER_ADMINdefault@domain.com

本文章主要介绍了应用最广最实用的重写功能，记住.htaccess的权限要设置成644

原文链接: .htaccess详解及.htaccess参数说明

©本文由 吕 收集整理，引用内容如有犯权请留言，转载请注明原文链接