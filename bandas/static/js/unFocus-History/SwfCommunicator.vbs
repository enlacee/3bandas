' unFocusFlashCommunicator, version 0.7 (alpha) (svn $Revision: 32 $) $Date: 2009-06-13 03:32:05 -0400 (Sat, 13 Jun 2009) $
' Copyright: 2005-2009, Kevin Newman (http://www.unfocus.com/)
'http://www.opensource.org/licenses/mit-license.php
Sub unFocusCreateFSCommand (FSCmdName)
	ExecuteGlobal "Sub " & FSCmdName & _
		"_FSCommand(ByVal c, ByVal a):" & _
		"call " & FSCmdName & "_DoFSCommand(c, a):" & _
		"End Sub"
End Sub