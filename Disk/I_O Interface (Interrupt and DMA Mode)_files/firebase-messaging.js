(function(){function firebaseMessagingWork(){if(checkForBrowser()){$(document).on('click','.notification-click',sendClickAnalyticsToServer);$(document).on('subscribeToExamTopics',subscribeToExamTopics);$(document).on('unsubscribeToExamTopics',unsubscribeToExamTopics);var config={apiKey:"AIzaSyCIBmK21QbFM79ClkC5_kuO882Xc9_dj7A",authDomain:"udofy-1021.firebaseapp.com",databaseURL:"https://udofy-1021.firebaseio.com",storageBucket:"udofy-1021.appspot.com",messagingSenderId:"1026789393376"};firebase.initializeApp(config);var token,tokenData=getLocalStorageData('tokenData'),messaging=firebase.messaging(),userId=$('input[name="userId"]').val();function sendTokenToServer(data){return $.ajax({method:"POST",url:"/user/editRegistrationId",data:JSON.stringify(data),dataType:'json',contentType:'application/json'});}
function subscribeToTopics(data){return $.ajax({method:"POST",url:"/fcm/subscribeUserToTopics",data:JSON.stringify(data),dataType:'json',contentType:'application/json'});}
function unsubscribeToTopics(data){return $.ajax({method:"POST",url:"/fcm/unsubscribeUserToTopics",data:JSON.stringify(data),dataType:'json',contentType:'application/json'});}
function initNotification(){return navigator.serviceWorker.register('/javascripts/web/app/firebase-messaging-sw.js?version=1.19').then(function(registration){messaging.useServiceWorker(registration);});}
function initiliazeNotification(){initNotification().then(function(){initSubscribeTopic();})}
initiliazeNotification();function requestPermission(){return messaging.requestPermission().then(function(){return messaging.getToken()}).then(function(tokenId){token=tokenId;return checkForTokenSent()}).then(function(resp){return saveTokenToLocalStorage(resp);});}
function initSubscribeTopic(){if(Notification.permission!=='granted'){return;}
requestPermission().then(function(resp){if(resp.error||!resp.regId){return;}
var topicsData=getLocalStorageData('topicsData');if(topicsData&&topicsData.regId!==resp.regId){subscribeTopics({deviceType:'web',regId:resp.regId,topics:topicsData.topics},true);}}).catch(function(err){console.log(err);});}
function getSubscribedExams(){if(!userId){return[];}
var exams=window.subscribedExamsData;var topics=[];if(exams&&exams.length>0){topics=exams.map(function(val){return window.getExamTag({id:val.examid,name:val.examname});});}
return topics;}
function subscribeToExamTopics(event){if(Notification.permission!=='granted'){return;}
var topics=[];var topicsData=getLocalStorageData('topicsData');if(topicsData&&topicsData.topics){topicsData=topicsData.topics;}
topicsData=topicsData||[];var exams=getSubscribedExams();exams.map(function(val){if(topicsData.indexOf(val)===-1){topics.push(val);}});if(topics.length===0){return;}
requestPermission().then(function(resp){if(resp.error||!resp.regId){return;}
subscribeTopics({deviceType:'web',regId:resp.regId,topics:topics});}).catch(function(err){console.log(err);});}
function unsubscribeToExamTopics(event){if(Notification.permission!=='granted'){return;}
var topicsData=getLocalStorageData('topicsData');if(topicsData&&topicsData.topics){topicsData=topicsData.topics;}
else{return;}
var exams=window.subscribedExamsData;var topics=[];if(exams&&exams.length>0){exams.forEach(function(val){var topicCheck=window.getExamTag({id:val.examid,name:val.examname});if(topicsData.indexOf(topicCheck)!==-1){topics.push(topicCheck);}});}
if(!topics.length){return;}
requestPermission().then(function(resp){if(resp.error||!resp.regId){return;}
unsubscribeTopics({deviceType:'web',regId:resp.regId,topics:topics});}).catch(function(err){console.log(err);});}
messaging.onTokenRefresh(function(){messaging.getToken().then(function(refreshedToken){token=refreshedToken;return checkForTokenSent()}).catch(function(err){console.log(err);});});messaging.onMessage(function(payload){if(!payload.notification){return;}
var bodyData;try{bodyData=JSON.parse(payload.notification.body);}
catch(e){bodyData={body:payload.notification.body,campaignName:"Gradeup Campaign",}}
var data={message:bodyData.body,action:{actionText:'<a class="notification-click" data-campaign="'+bodyData.campaignName+'" href="'+payload.notification.click_action+'" target="_blank">Open</a>'}}
createToast(data);});function saveTokenToLocalStorage(resp){if(resp&&resp.alreadySent){return $.Deferred().resolve(resp);}
if(resp.error){console.log(error);return $.Deferred().resolve(resp);}
if(tokenData===null){tokenData={};}
var date=new Date();date=date.setHours(0,0,0,0);tokenData={regId:token,date:date,}
if(!resp.userLoggedOut){tokenData.userId=userId;}
setLocalStorageData('tokenData',tokenData);return $.Deferred().resolve(tokenData);}
function checkForTokenSent(){var date=new Date();date=date.setHours(0,0,0,0);if(tokenData!==null){if(tokenData.userId===userId&&tokenData.regId===token&&(date-(24*60*60*1000))<(+tokenData.date)){return $.Deferred().resolve({alreadySent:true,regId:token});}}
if(userId&&token){return sendTokenToServer({registrationId:token,deviceType:'web'})}
else{return $.Deferred().resolve({userLoggedOut:true,regId:token});}}
function subscriber(topic){if(!topic){return Promise.reject({message:"No Topic provided!"});}
if(Notification.permission==='granted'){return messaging.getToken().then(function(token){var topics=[];var topicsData=getLocalStorageData('topicsData');if(topicsData&&topicsData.topics){topicsData=topicsData.topics;}
topicsData=topicsData||[];var exams=getSubscribedExams();exams.map(function(val){if(topicsData.indexOf(val)===-1){topics.push(val);}});topics.push(topic);var data={regId:token,topics:[topic],deviceType:'web'};return subscribeTopics(data);}).then(function(resp){if(resp&&resp.error){console.log(resp.error);return resp;}
createToast({closeButton:true,message:"You have been subscribed to this topic!"});return resp;}).catch(function(err){console.log(err);return err;});}
else{return requestPermission().then(function(resp){var topics;var topicsData=getLocalStorageData('topicsData');if(topicsData&&topicsData.regId!==resp.regId){topics=topicsData.topics;}
topics=topics||[];var exams=getSubscribedExams();exams.map(function(val){if(topics.indexOf(val)===-1){topics.push(val);}});topics.push(topic);var data={regId:resp.regId,topics:topics,deviceType:'web'};return subscribeTopics(data);}).then(function(resp){if(resp&&resp.error){console.log(resp.error);return resp;}
createToast({closeButton:true,message:"You have been subscribed to this topic!"});return resp;}).catch(function(err){console.log(err);return err;});}}
function subscribeTopics(data,flag){return subscribeToTopics(data).then(function(response){var topicsData=getLocalStorageData('topicsData');if(topicsData){if(!flag){data.topics.forEach(function(val){if(topicsData.topics.indexOf(val)===-1){topicsData.topics.push(val);}});}
if(topicsData.regId!==data.regId){topicsData.regId=data.regId;}}
else{topicsData={regId:data.regId,topics:data.topics};}
setLocalStorageData('topicsData',topicsData);return response;});}
function unsubscribeTopics(data){return unsubscribeToTopics(data).then(function(response){var topicsData=getLocalStorageData('topicsData');if(topicsData&&topicsData.topics){data.topics.forEach(function(val){if(topicsData.topics.indexOf(val)!==-1){topicsData.topics.splice(topicsData.topics.indexOf(val),1);}});if(topicsData.regId!==data.regId){topicsData.regId=data.regId;}}
setLocalStorageData('topicsData',topicsData);return response;});}
function sendClickAnalyticsToServer(event){var campaignName=$(this).attr('data-campaign');var payload={v:1,tid:'UA-80480423-1',ds:'serviceworker',t:'event',ec:'WebNotification',ea:'WebNotificationClicked',el:campaignName,};var payloadString=Object.keys(payload).map(function(analyticsKey){return analyticsKey+'='+encodeURIComponent(payload[analyticsKey]);}).join('&');fetch('https://www.google-analytics.com/collect',{method:'POST',body:payloadString,}).then(function(response){console.log("Analytics Clicked Data Captured");}).catch(function(response){console.log("Analytics Clicked Data Cannot Be Captured");})}
function getLocalStorageData(key){try{return JSON.parse(window.localStorage.getItem(key));}
catch(e){return{};}}
function setLocalStorageData(key,data){if(key==='topicsData'){window.topicsSubscribed=data;}
window.localStorage.setItem(key,JSON.stringify(data));}
window.topicsSubscribed=getLocalStorageData('topicsData');window.subscriber=subscriber;}}
function checkForBrowser(){if((/Firefox[\/\s](\d+\.\d+)/.test(navigator.userAgent))||(/Chrome/.test(navigator.userAgent)&&/Google Inc/.test(navigator.vendor))){return true;}
return false;}
window.checkForBrowser=checkForBrowser;firebaseMessagingWork();})();