importScripts("https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/9.23.0/firebase-messaging-compat.js");


const config = {
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


console.log('in service worker - after firebase.messaging');


messaging.onBackgroundMessage(function(payload) {
    console.log('백그라운드 메시지 수신:', payload);
  
    const notificationTitle = 'HEARo';
    const notificationOptions = {
      body: '응급상황 발생'
    };
  
    registration.showNotification(notificationTitle, notificationOptions);
});

messaging.onMessage(function(payload) {
    console.log('백그라운드 메시지 수신:', payload);
  
    const notificationTitle = 'HEARo';
    const notificationOptions = {
      body: '응급상황 발생'
    };
  
    registration.showNotification(notificationTitle, notificationOptions);
});

self.addEventListener('activate', messaging.onMessage(function(payload) {
    console.log('Recieved background message');
    const title = "HEARo";
    const options = {
        body: "응급상황 발생"
    }
    var notification = new Notification(title, options);
    })
);

self.addEventListener('activate', messaging.onBackgroundMessage(function(payload) {
    console.log('Recieved background message');
    const title = "HEARo";
    const options = {
        body: "응급상황 발생"
    }
    var notification = new Notification(title, options);
    })
);