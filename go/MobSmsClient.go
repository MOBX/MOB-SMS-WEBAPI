// Package: default
// File: MobSmsClient.go
// Created by: luckscript(luckscript@gmail.com)
// DATE: 17-4-17 18:01
package main
import (
	"net/http"
	"io/ioutil"
	"net/url"
    "fmt"
 )
// bingone
func main(){

	// 修改为您的appkey.在官网（http://www.mob.com)登录后获取,接口地址联系客服
	apikey 		:= "xxxxxxxxxxxxxxxxxx"
	// 修改为您要发送的手机号码
	phone 		:= "18912386146"
	// 国家代码
	zone 		:= "86"
	// 手机收到的短信验证码code
	code		:= "1234"
	
	// Web-Api验证码发送接口
	url_webapi_send_uri	  := "https://xxxxxxxxxxxxxxxxxx";
	// Web-Api验证码校验接口
	url_webapi_check_uri  := "https://xxxxxxxxxxxxxxxxxx";
	// 短信服务端验证接口
	url_webapi_verify_uri := "https://xxxxxxxxxxxxxxxxxx";


	data_webapi_send_uri	:= url.Values{"appkey": {apikey}, "phone": {phone},"zone":{zone}}
	data_webapi_check_uri	:= url.Values{"appkey": {apikey}, "phone": {phone},"zone":{zone},"code":{code}}
	data_webapi_verify_uri	:= url.Values{"appkey": {apikey}, "phone": {phone},"zone":{zone},"code":{code}}


	httpsPostForm(url_webapi_send_uri,data_webapi_send_uri)
	httpsPostForm(url_webapi_check_uri,data_webapi_check_uri)
	httpsPostForm(url_webapi_verify_uri,data_webapi_verify_uri)
}

func httpsPostForm(url string,data url.Values) {
	resp, err := http.PostForm(url,data)

	if err != nil {
		// handle error
	}

	defer resp.Body.Close()
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		// handle error
	}

	fmt.Println(string(body))

}
