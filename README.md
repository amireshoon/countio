# Countio
Ready to use count api alternative for count.io
Some usage can be like counter for static sites deployed on vercel or serverless sites to count visitors or planty of other things.

# Usage
```js
$.ajax({
url:"https://countio.herokuapp.com/count/<hid>/+",
type: "POST",
success: function(data) {
  alert(data.count);
}
});
```

# Endpoints
Do not share app name with others and for increase and decrease count value use app `hid`.
API base url: https://countio.herokuapp.com
| Endpoints                  	| Operation            	| Parameters      	| Returns                 	|
|----------------------------	|----------------------	|-----------------	|-------------------------	|
| /new/account/{app_name}    	| Creates new app      	| string app name 	| app name and hid        	|
| /remove/account/{app_name} 	| Remove existing app  	| string app name 	|                         	|
| /count/{hid}/+             	| Increase count value 	| string hid      	| new count value and hid 	|
| /count/{hid}/-             	| Decrease count value 	| string hid      	| new count value and hid 	|
