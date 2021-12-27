<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Tổng hợp tìm hiểu (Flyhigh Team)</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
}

.simple-table-header {
	background: rgb(247, 246, 243);
	color: black;
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(145, 145, 142, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(187, 132, 108, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(215, 129, 58, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 148, 51, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(108, 155, 125, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(91, 151, 189, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(167, 130, 195, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(205, 116, 159, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(225, 111, 100, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(145, 145, 142, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(187, 132, 108, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(215, 129, 58, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 148, 51, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(108, 155, 125, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(91, 151, 189, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(167, 130, 195, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(205, 116, 159, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(225, 111, 100, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="31ed6bcb-48b8-4e2d-b2f5-876581ab2a59" class="page sans"><header><h1 class="page-title">Tổng hợp tìm hiểu (Flyhigh Team)</h1></header><div class="page-body"><h1 id="adbf13b0-584e-4924-bbd2-1036258ac65c" class="">1. OCR</h1><ol type="1" id="b0e6824f-5a81-4a5d-a560-1e8ebf80c5b1" class="numbered-list" start="1"><li>Thông tin<ul id="59c93c9b-783a-454f-ab6d-e9ce07a016c1" class="bulleted-list"><li style="list-style-type:disc">App: VietOCR.</li></ul><ul id="65dc986b-6777-4e4f-ab92-83de2d966137" class="bulleted-list"><li style="list-style-type:disc">Độ chính xác rất cao: 90% → 95%</li></ul><ul id="b95d3240-6072-4447-b566-2436506fda83" class="bulleted-list"><li style="list-style-type:disc">Các chức năng: OCR hình ảnh sang file txt, có chức năng chuyển nhiều file cùng 1 lúc.</li></ul><ul id="869d521c-70de-45c2-bbe4-c7e6e411260a" class="bulleted-list"><li style="list-style-type:disc">Hỗ trợ đồng thời tiếng Anh và tiếng Việt</li></ul></li></ol><ol type="1" id="a4e603dd-d825-4ec6-9acf-3e3830dc0413" class="numbered-list" start="2"><li>Cách cài đặt<ul id="8e2b55fe-0a5f-42b6-a560-bb2949863593" class="bulleted-list"><li style="list-style-type:disc">Link download phần mềm: <a href="https://sourceforge.net/projects/vietocr/">https://sourceforge.net/projects/vietocr/</a> </li></ul><ul id="4a7fba36-733e-4641-92ee-59b9201a822f" class="bulleted-list"><li style="list-style-type:disc">Tải về và cài đặt như bình thường</li></ul></li></ol><ol type="1" id="40ff61b5-3896-4a5e-977c-519851be23ab" class="numbered-list" start="3"><li>Sử dụng<ul id="bbe58f0c-ca45-4fa1-9698-775c2b1377ab" class="bulleted-list"><li style="list-style-type:disc">Màn hình khởi động<figure id="873ac75f-45ee-4266-a986-df546a3358b0" class="image"><a href="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled.png"><img style="width:960px" src="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled.png"/></a></figure></li></ul><ul id="65c8933e-5d82-428f-b8ad-44999bcdb4cb" class="bulleted-list"><li style="list-style-type:disc">Nếu OCR 1 file, kéo thả file vào vùng làm việc của ứng dụng và chọn Image→OCR all page<figure id="51bd852b-7cd7-4828-8660-b12b948c49db" class="image"><a href="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled%201.png"><img style="width:960px" src="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled%201.png"/></a><figcaption>Result</figcaption></figure></li></ul><ul id="fa660d7d-8c81-4142-b15c-24dcb1e5438f" class="bulleted-list"><li style="list-style-type:disc">OCR nhiều file, chọn Image→Bulk OCR, sau đó điền folder input và output rồi enter<figure id="f6d30411-4559-4ac2-bd00-a15e82585519" class="image"><a href="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled%202.png"><img style="width:960px" src="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled%202.png"/></a></figure><figure id="70da1f28-63ef-469e-8bfd-615d5e4e382b" class="image"><a href="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled%203.png"><img style="width:960px" src="To%CC%82%CC%89ng%20ho%CC%9B%CC%A3p%20ti%CC%80m%20hie%CC%82%CC%89u%20(Flyhigh%20Team)%20873ac75f45ee4266a986df546a3358b0/Untitled%203.png"/></a><figcaption>Kết quả sau khi thử nghiệm OCR nhiều file</figcaption></figure></li></ul><h1 id="2f22bb7e-f25e-40e2-a993-0a68769058e5" class="">2. Xử lí ngôn ngữ tự nhiên (NLP)</h1><h2 id="5562a070-3eee-4bd3-aee7-704ab1d34262" class="">I. Tiếng Anh</h2><ol type="1" id="ee486f84-7cc0-45ff-9251-2b36fabf6b55" class="numbered-list" start="1"><li>Thông tin<ul id="a8814a9f-35ac-48f8-aa12-685a89959b75" class="bulleted-list"><li style="list-style-type:disc">App: NLTK (Python)</li></ul><ul id="16a37cbc-8ee1-4820-a750-9a2261cb4c8a" class="bulleted-list"><li style="list-style-type:disc">Chức năng: Phân tích từ loại, loại bỏ stopword.</li></ul><ul id="74d4032b-95bf-41a2-9c74-fb1bbde9e9d0" class="bulleted-list"><li style="list-style-type:disc">Ngôn ngữ hỗ trợ: Tiếng Anh</li></ul></li></ol><ol type="1" id="d151448d-1da5-4e94-b573-01c8b5432dc0" class="numbered-list" start="2"><li>Cài đặt<pre id="5bb31b1a-f9f3-444f-83ea-fb86d38ec8fe" class="code"><code>python -m pip install nltk
nltk.download()</code></pre></li></ol><ol type="1" id="87d6c5ba-533a-496b-bfc6-386a2033a542" class="numbered-list" start="3"><li>Source code<ul id="e9f28b31-fafc-4eb6-81fa-958b2277e0f8" class="bulleted-list"><li style="list-style-type:disc">Testing with model text<ul id="139ab66c-c980-4280-bc4d-518e79c4e46c" class="bulleted-list"><li style="list-style-type:circle">test.py</li></ul><pre id="a1cba477-7e7d-4107-98d9-f5fab36d2d1b" class="code"><code>from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_sent = &quot;&quot;&quot;This is a sample sentence,
                  showing off the stop words filtration.&quot;&quot;&quot;
 
stop_words = set(stopwords.words(&#x27;english&#x27;))
 
word_tokens = word_tokenize(example_sent)
 
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)</code></pre><p id="7aa5ed6e-aa49-4bfe-af6e-e5e4b3f54918" class="">→ Output: </p><pre id="99c45dba-ba00-4fd7-938b-f9df26df6cb2" class="code"><code>[&#x27;This&#x27;, &#x27;is&#x27;, &#x27;a&#x27;, &#x27;sample&#x27;, &#x27;sentence&#x27;, &#x27;,&#x27;, &#x27;showing&#x27;, 
&#x27;off&#x27;, &#x27;the&#x27;, &#x27;stop&#x27;, &#x27;words&#x27;, &#x27;filtration&#x27;, &#x27;.&#x27;]
[&#x27;This&#x27;, &#x27;sample&#x27;, &#x27;sentence&#x27;, &#x27;,&#x27;, &#x27;showing&#x27;, &#x27;stop&#x27;,
&#x27;words&#x27;, &#x27;filtration&#x27;, &#x27;.&#x27;]</code></pre></li></ul><ul id="93ca31d1-1197-48cb-9e72-ad7c637deb09" class="bulleted-list"><li style="list-style-type:disc">Testing with file txt<ul id="ffc11f06-d8ff-41f8-8561-340eb4ed63fe" class="bulleted-list"><li style="list-style-type:circle">Source code:</li></ul><pre id="85f2483a-f2f5-45eb-bd31-d0d1ef3ba4a4" class="code"><code>import io
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
dir = sys.argv[1]

# word_tokenize accepts
# a string as an input, not a file.
stop_words = set(stopwords.words(&#x27;english&#x27;))
file1 = open(dir)
 
# Use this to read file content as a stream:
line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open(&#x27;filteredtext.txt&#x27;,&#x27;a&#x27;)
        appendFile.write(&quot; &quot;+r)
        appendFile.close()</code></pre><ul id="0c79aab1-e8bb-4ed2-8817-63f99e90a2cd" class="bulleted-list"><li style="list-style-type:circle">Input: python <a href="http://nlp.py">nlp.py</a> test.txt</li></ul><ul id="fb646676-d01e-438e-8281-235de2d43c29" class="bulleted-list"><li style="list-style-type:circle">Output: filteredtext.txt</li></ul></li></ul></li></ol><h2 id="a0d48381-1bc0-4844-bf17-1b4a98199190" class="">II. Tiếng Việt</h2><ol type="1" id="0ed8e16f-501d-4793-91fc-0f5a43b80f41" class="numbered-list" start="1"><li>Thông tin<ul id="8b14f449-2014-41d1-b7c4-1209fe42a69f" class="bulleted-list"><li style="list-style-type:disc">App: UndertheseaNLP (Python)</li></ul><ul id="53285165-1bdd-4eea-aa9f-719cfa5ccb86" class="bulleted-list"><li style="list-style-type:disc">Chức năng: Phân tích từ loại, loại bỏ stopword.</li></ul><ul id="b3b9aac2-e82e-49d8-98f7-15b9557589d6" class="bulleted-list"><li style="list-style-type:disc">Ngôn ngữ hỗ trợ: Tiếng Việt</li></ul></li></ol><ol type="1" id="ed4eb487-01fd-4022-a9ad-6be95f204b1e" class="numbered-list" start="2"><li>Source Code<pre id="e0dd3054-6d50-4d25-b2b0-9e113f2fd012" class="code"><code>import io
import sys
import os
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
import codecs
import array as arr




from nltk.corpus import stopwords
from underthesea import word_tokenize #Use &#x27;underthesea lib&#x27; instead of &#x27;nltk&#x27; for better result
 

dir = sys.argv[1]
with io.open(dir,&#x27;r&#x27;,encoding=&#x27;utf8&#x27;) as file:
    text = file.read().replace(&#x27;\n&#x27;, &#x27;&#x27;)
text = word_tokenize(text)


stop_words = set(stopwords.words(&#x27;vietnamese&#x27;))
  
filtered_sentence = [w for w in text if not w.lower() in stop_words]
 
filtered_sentence = []
 
for w in text:
    if w not in stop_words:
        filtered_sentence.append(w)
 

print(filtered_sentence)



for r in filtered_sentence:
    with io.open(&#x27;filteredtext.txt&#x27;,&#x27;a&#x27;,encoding=&#x27;utf8&#x27;) as file:
        file.write(r + &quot; &quot;)
        file.close()</code></pre><p id="00190b90-a677-42b1-b5f2-bd4df267c948" class="">
</p><p id="4f00dbee-61b9-4000-80be-45f390afbff6" class="">
</p></li></ol><p id="09ced268-ad56-4fe2-bdbe-b683b7b820a9" class="">
</p></li></ol><h1 id="d5c088ce-ee52-4331-87f1-4ac44e88f8c0" class="">3. Tìm kiếm trong 2000 tệp văn bản (Đã OCR sang file .txt)</h1><div><h2 id="28fc8466-93d0-4917-b18d-4256d2cef133" class="">I. Tiếng Anh &amp; Tiếng Việt</h2><ol type="1" id="a783a25d-ba51-4abb-b06a-f3a280432da8" class="numbered-list" start="1"><li>Source code<pre id="80c4a490-4338-46f9-99c4-0378cbdd8ce0" class="code"><code>import io
import sys
import os
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
import codecs
import array as arr

types_of_encoding = [&quot;utf8&quot;, &quot;cp1252&quot;]
def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()
dir = sys.argv[1]
dir2 = sys.argv[2]


with io.open(dir,&#x27;r&#x27;,encoding=&#x27;utf8&#x27;) as file:
    data = file.read().replace(&#x27;\n&#x27;, &#x27;&#x27;)


# get file ketqua.txt
# os.chdir(dir2)
os.system(&#x27;dir /b /a-d &#x27;+ dir2+ &quot; &gt; 5e95d803.tmp&quot;)
#dir folder 
fo = open(&quot;5e95d803.tmp&quot;, &quot;r&quot;)
tmps = []
with open (&quot;5e95d803.tmp&quot;) as textFile:
    for line in textFile:
        tmp = line.strip()
        tmps.append(tmp)
#get list of file to tmps array
fo.close()
os.remove(&quot;5e95d803.tmp&quot;)
os.chdir(dir2)
ratiocalc = 0
ratioMAX = 0
i = 0
ratioarray = []
name = []
for x in tmps:
    with io.open(x,&#x27;r&#x27;,encoding=&#x27;utf8&#x27;) as file199111:
        dataclone = file199111.read().replace(&#x27;\n&#x27;, &#x27;&#x27;)
        tmp1234 = similar (data, dataclone) 
        ratioarray.append(tmp1234)
        name.append(x)



#so sánh
for j in range(len(ratioarray)):
    #initially swapped is false
    swapped = False
    i = 0
    while i&lt;len(ratioarray)-1:
        #comparing the adjacent elements
        if ratioarray[i]&lt;ratioarray[i+1]:
            #swapping
            name[i],name[i+1] = name[i+1],name[i]
            ratioarray[i],ratioarray[i+1] = ratioarray[i+1],ratioarray[i]
            
            #Changing the value of swapped
            swapped = True
        i = i+1
    #if swapped is false then the list is sorted
    #we can stop the loop
    if swapped == False:
        break

unique_l = sorted(set(name), key=name.index)

print (&quot;Files that are most similar to the given content&quot;)
for i in range(len(unique_l)):
    print (unique_l[i])
    if i == 4:
        break</code></pre></li></ol><ol type="1" id="aed5fa77-89f3-4200-b307-cd6ff13b9bbf" class="numbered-list" start="2"><li>Example<p id="074100e4-0f2e-4914-b835-15d9d4375722" class="">INPUT: </p><pre id="d710d1af-47da-49d8-960f-a377f78a1c3b" class="code"><code>python NLP_Search_Files_ENG.py filteredtext.txt ocr_results</code></pre><figure class="block-color-gray_background callout" style="white-space:pre-wrap;display:flex" id="f46f6657-f35c-4b5f-84ad-b222ee99eaaf"><div style="font-size:1.5em"><span class="icon">💡</span></div><div style="width:100%">Note: 
- NLP_Search_ENG.py: python file
- filteredtext.txt: text file after remove stopwords
- ocrresults\ : folder txt to search in this</div></figure><p id="bfc74da7-ce27-4926-baf9-19c6d63bb74d" class="">OUTPUT:</p><pre id="f9c6271d-1093-42aa-acc3-dd2407c7a4a0" class="code"><code>Files that are most similar to the given content
[1]Harry Potter and the Philosopher-s Stone_Page_013.jpg.txt
[1]Harry Potter and the Philosopher-s Stone_Page_215.jpg.txt
[1]Harry Potter and the Philosopher-s Stone_Page_008.jpg.txt
[1]Harry Potter and the Philosopher-s Stone_Page_143.jpg.txt
[1]Harry Potter and the Philosopher-s Stone_Page_214.jpg.txt</code></pre></li></ol></div><h1 id="eec3ae1b-2e65-47fa-8c9d-272914520e37" class="">4. Tìm kiếm tài liệu có nội dung tương tự trên Internet</h1><h2 id="e57742a9-efff-45a3-a679-1ea0d92b9dff" class="">Tiếng Anh và Tiếng Việt</h2><ol type="1" id="a901f0c1-835e-47bf-b9e7-b5edc76e8391" class="numbered-list" start="1"><li>Thông tin<ul id="23396ae8-f8db-4855-b670-a84490e5958b" class="bulleted-list"><li style="list-style-type:disc">App: Magic_Google (Github)</li></ul><ul id="b0a3f2d7-3c36-4955-a639-169d04c3b5c8" class="bulleted-list"><li style="list-style-type:disc">Chức năng: Trích xuất nội dung từ file txt và tìm kiếm nội dung đó trên Internet</li></ul></li></ol><ol type="1" id="eb9cc767-b97c-4e7b-b74c-73108461e8fb" class="numbered-list" start="2"><li>Source code<pre id="e6005bc2-3d41-468b-a554-7ccecfdc26cb" class="code"><code>import io
import sys


from magic_google import MagicGoogle
import pprint
import io
import sys
import os
import subprocess
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from difflib import SequenceMatcher
import codecs
import array as arr
types_of_encoding = [&quot;utf8&quot;, &quot;cp1252&quot;]
def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()
dir = sys.argv[1]

with open(dir, &#x27;r&#x27;) as file:
    data = file.read().replace(&#x27;\n&#x27;, &#x27;&#x27;)

PROXIES = []

mg = MagicGoogle(PROXIES)


for url in mg.search_url(query=data):
    pprint.pprint(url)
    #####################################################################</code></pre><p id="73f7121c-51e8-446d-995f-d0957cefa28f" class="">
</p></li></ol></div></article></body></html>