# 
# ASPermissionRequest.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init screen ASPermissionRequest(bundleName="AS_APP_BUNDLE", requestingFor, onDeclineRequest=Return(1), onAcceptRequest=Return(0)):
    tag ASPermissionRequest
    style_prefix "ASPermissionRequest"
    zorder 100
    modal True
    
    on "show":
        action [
            Function(SetThumbnailFull),
            FileTakeScreenshot(),
            Function(SetThumbnailOriginal)
        ]
    
    add FileCurrentScreenshot() at blur

    add AS_FRAMEWORK_DIR("AppKit") + "/Resources/ASPermissionRequestBackground.png"


    frame:
        style "ASPermissionRequestFrame"
        xalign 0.5
        yalign 0.5

        has vbox:
            xalign 0.5
            yalign 0.5
            xsize 656
            spacing 16

            text bundleName + " Would Like To " + AS_REQUIRE_PERMS_NAME[requestingFor]:
                style "ASPermissionRequestTitle"
            text AS_REQUIRE_PERMS_DESC[requestingFor]:
                style "ASPermissionRequestDetail"

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Don't Allow") action onDeclineRequest:
                    style "ASPermissionRequestDeclinedButton"
                textbutton _("Allow") action onAcceptRequest:
                    style "ASPermissionRequestAcceptButton"

