
var toast = cordova.require('toast');

function writeTag(nfcEvent) {
  // ignore what's on the tag for now, just overwrite
    
  var mimeType = document.forms[0].elements["mimeType"].value,
    payload = document.forms[0].elements["payload"].value,
    record = ndef.mimeMediaRecord(mimeType, nfc.stringToBytes(payload));

  nfc.write(
        [record], 
        function () {
            toast.showShort("Wrote data to tag.");
						console.log("Wrote data to tag.");
            //navigator.notification.vibrate(100);
        }, 
        function (reason) {
            console.log("There was a problem : " + reason);
        }
  );   
}

var app = {
	
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
		
    // Bind Event Listeners
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
				document.addEventListener("menubutton", showSampleData, false);
    },
		
    // deviceready Event Handler
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
				console.log('\n\n\n\n\n\nStart IndawoPro\n');
			
				// Read NDEF formatted NFC Tags
		    nfc.addTagDiscoveredListener (
						writeTag,
		        function () { // success callback
		            console.log("Listening for NDEF tags");
		        },
		        function (error) { // error callback
								alert('Failed to register NFC Listener');
		        }
		    );
			
    },
		
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};

app.initialize();

var data = [
    {
        mimeType: 'text/plain',
        payload: 'Hello PhoneGap'
    },
    {
        mimeType: 'text/pg',
        payload: 'Hello PhoneGap'
    },
    {
        mimeType: 'text/x-vCard',
        payload: 'BEGIN:VCARD\n' +
            'VERSION:2.1\n' +
            'N:Coleman;Don;;;\n' +
            'FN:Don Coleman\n' +
            'ORG:Chariot Solutions;\n' +
            'URL:http://chariotsolutions.com\n' +
            'TEL;WORK:215-358-1780\n' +
            'EMAIL;WORK:dcoleman@chariotsolutions.com\n' +
            'END:VCARD'
    },
    {
        mimeType: 'text/x-vCard',
        payload: 'BEGIN:VCARD\n' +
            'VERSION:2.1\n' +
            'N:Griffin;Kevin;;;\n' +
            'FN:Kevin Griffin\n' +
            'ORG:Chariot Solutions;\n' +
            'URL:http://chariotsolutions.com\n' +
            'TEL;WORK:215-358-1780\n' +
            'EMAIL;WORK:kgriffin@chariotsolutions.com\n' +
            'END:VCARD'
    },
    {
        mimeType: 'game/rockpaperscissors',
        payload: 'Rock'
    },
    {
        mimeType: '',
        payload: ''
    }
];

var index = 0;
function showSampleData() {
    var mimeTypeField = document.forms[0].elements["mimeType"],
      payloadField = document.forms[0].elements["payload"],
      record = data[index];
    
    index++;
    if (index >= data.length) {
        index = 0;
    }
    
    mimeTypeField.value = record.mimeType;
    payloadField.value = record.payload;    
}