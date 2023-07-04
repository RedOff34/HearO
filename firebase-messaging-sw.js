importScripts("https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging-compat.js");


// Initialize Firebase
var config = {
    apiKey: "AIzaSyDgtSjvTOyVl0K0mgPmahTP9ztjAgr6k1I",
    authDomain: "hearo-78135.firebaseapp.com",
    databaseURL: "https://hearo-78135-default-rtdb.firebaseio.com",
    projectId: "hearo-78135",
    storageBucket: "hearo-78135.appspot.com",
    messagingSenderId: "204455560154",
    appId: "1:204455560154:web:0516adb61f9b2fde45b6e3",
    measurementId: "G-FQ7E4135WX"
};
console.log('in service worker - before initializeApp');
firebase.initializeApp(config);
console.log('in service worker - after initializeApp');

const messaging = firebase.messaging();

messaging.getToken({vapidKey:"BEbTVF3r7CQqh5r-tPrCxxjeTem-oJNh9POmkm8LgAc4nPy-Hd6lxKl6gHWCo2aRjrdlOfmVM272b5-W9N95t54"})
.then(function(token){
    console.log(token);
})
.catch(function(arr){
    console.log("Error Occured");
});

console.log('in service worker - after firebase.messaging');

messaging.onMessage(function(payload) {
    console.log('Recieved background message');
    const title = "HEARo";
    const options = {
        body: "응급상황 발생"
    }
    return self.registration.showNotification(title, options);
});

// if the app is in the background (user not on page)
messaging.onBackgroundMessage(function(payload) {
    console.log('Recieved background message');
    const title = "HEARo";
    const options = {
        body: "응급상황 발생"
    }
    return self.registration.showNotification(title, options);
});