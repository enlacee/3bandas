        // My mini "Ajax" (DHTML) app
        function PromptMe() {
            // some application vars
            var stateVar = "nothin'", displayDiv = document.getElementById("contentAjax");

            // the sole public method to manipulate this application
            this.promtForNew = function(elemento) {

                var id = elemento.getAttribute('history');//attributes.rel.value; 
                //alert("id = "+id);
                unFocus.History.addHistory(id);
            };



            this.historyListener = function(historyHash) {

                stateVar = historyHash;
                // update display content
                displayDiv.innerHTML = "Current Historyx: " + historyHash;
                // update document title
                document.title = location.hostname +"  "+ historyHash;
            };


            // subscribe to unFocus.History
            unFocus.History.addEventListener('historyChange', this.historyListener);

            // Check for an initial value (deep link).
            // In this demo app, the historyListener can handle the task.
            this.historyListener(unFocus.History.getCurrent());
        };