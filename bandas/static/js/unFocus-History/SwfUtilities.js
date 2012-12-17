/*
unFocusFlash.Utilities, version 0.5 (svn $Revision: 32 $) $Date: 2009-06-13 03:32:05 -0400 (Sat, 13 Jun 2009) $
Copyright: 2005-2009, Kevin Newman (http://www.unfocus.com/)
http://www.opensource.org/licenses/mit-license.php
*/
if (!window.unFocus) var unFocus = {};
if (!unFocus.SwfUtilities) unFocus.SwfUtilities = {
	getSwfReference: function(swfId) {
		var $movieObj;
		if (document.embeds && document.embeds[swfId])
			$movieObj = document.embeds[swfId];
		 else if (document[swfId])
			$movieObj = document[swfId];
		 /*else if (window[$swfId])
			$movieObj = $window[$swfId];
		else if (document.getElementById)
			$movieObj = document.getElementById($swfId);*/
		return $movieObj;
	}
};
