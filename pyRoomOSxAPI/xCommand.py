class Top_Level:
    def __init__(self) -> str:
        pass

    def xCommand_Dial_Appearance:_value,_BookingId:_value,_CallRate:_value,_CallType:_value,_DisplayName:_value,_Number:_value,_Protocol:_value,_TrackingData:_value():
            pass

        '''
            Dial out from the device. Returns information about the CallId and ConferenceId, which are required for some of the other commands.
        '''
class Audio:
    def __init__(self) -> str:
        pass

    def xCommand_Audio_Select_Device:_value():
            pass

        '''
            Select which type of audio device to use (built-in loudspeakers and microphone, headsets, or handset).
        '''
    def xCommand_Audio_Diagnostics_MeasureDelay_MeasurementLength:_value,_Output:_value,_Volume:_value():
            pass

        '''
            This command measures the audio delay/latency in a device that is connected to the video conferencing device. A typical use case it to measure the delay in a TV connected to the video conferencing device via the HDMI connector. If the delay in a TV is too high, the real-time experience of a video call will be substantially degraded. If the delay is more than 50 ms we recommend the user to find a TV setting that has shorter delay. Typical TV settings that can reduce the delay are: Gaming Mode and...
        '''
    def xCommand_Audio_Diagnostics_Advanced_Run_Channel:_value,_MeasurementLength:_value,_Output:_value,_Volume:_value():
            pass

        '''
            This command sends out a noise signal sequentially on all audio output connectors and measures the room impulse response (RIR) between the output and the microphones. If a RIR is detected, the detected number of microphones (input), the detected number of output connectors, and the detected delay between the output and input is reported back. Example: xCommand Audio Diagnostics Advanced Run Volume: 50 MeasurementLength: 1 Result returned -> OK *r AdvancedRunResult (status=OK): *r AdvancedRunResu...
        '''
        class AecReverb:
            pass

            def Reset():
            pass

        '''
            Reset the acoustic echo cancellation. This command is useful when making changes in the acoustical treatment of the room. All previous adaptations are cleared and a new measurement of the reverberation time is made. This is not allowed during a call.
        '''
            def Run():
            pass

        '''
            The command uses the acoustic echo canceller to give an estimate of the reverberation time in the room. This is done transparently, without interruption of the normal operation of the endpoint.
        '''
    class Microphones:
        pass

        def Mute():
            pass

        '''
            Mute all microphones.
        '''
        def ToggleMute():
            pass

        '''
            Toggle the microphone between muted and unmuted.
        '''
        def Unmute():
            pass

        '''
            Unmute all microphones.
        '''
        class MusicMode:
            pass

            def Start():
            pass

        '''
            Start using MusicMode in the current call. Music mode allows the dynamic range of music go through. When Music mode is in use, sound level variations are transmitted intact and the noise filtering is kept to a minimum. MusicMode is automatically turned off when the call ends.
        '''
            def Stop():
            pass

        '''
            Stop using MusicMode in the current call.
        '''
        class NoiseRemoval:
            pass

            def Activate():
            pass

        '''
            Activate noise removal on the device. For this to take effect, you need to enable xConfiguration Audio Microphones NoiseRemoval Mode to enable the noise removal feature on the device.
        '''
            def Deactivate():
            pass

        '''
            Deactivate noise removal on the device.
        '''
    def xCommand_Audio_Sound_Play_Loop:_value,_Sound:_value():
            pass

        '''
            Play a specified audio sound.
        '''
    class Sound:
        pass

        def Stop():
            pass

        '''
            Stop playing audio sound.
        '''
        class Ringtone:
            pass

            def List():
            pass

        '''
            List all available ringtones. Use the xConfiguration Audio SoundsAndAlerts RingTone setting to choose a ringtone.
        '''
    def xCommand_Audio_SoundsAndAlerts_Ringtone_Play_Loop:_value,_RingTone:_value():
            pass

        '''
            Play one of the available ringtones. Use the xCommand Audio SoundsAndAlerts Ringtone List command to get a list of the available ringtones.
        '''
            def Stop():
            pass

        '''
            Stops the chosen ringtone from playing. To start playing the ringtone again, use the Audio SoundsAndAlerts Ringtone Play xCommand.
        '''
    def xCommand_Audio_Volume_Decrease_Device:_value,_Steps:_value():
            pass

        '''
            Decrease the volume on one of the video conferencing device's audio units (built-in loudspeakers, headsets, or handset). By default, the volume is decreased by 5 steps (each step is 0.5 dB). Use the Steps parameter if you want to override the default behavior. You can use the optional Device parameter to specify which audio unit to address. The most recently selected unit is chosen if you don't specify a unit (see xStatus Audio SelectedDevice). Also refer to xCommand Audio Select.
        '''
    def xCommand_Audio_Volume_Increase_Device:_value,_Steps:_value():
            pass

        '''
            Increase the volume on one of the video conferencing device's audio units (built-in loudspeakers, headsets, or handset). By default, the volume is increased by 5 steps (each step is 0.5 dB). Use the Steps parameter if you want to override the default behavior. You can use the optional Device parameter to specify which audio unit to address. The most recently selected unit is chosen if you don't specify a unit (see xStatus Audio SelectedDevice). Also refer to xCommand Audio Select.
        '''
    class Volume:
        pass

        def Mute():
            pass

        '''
            Mute the volume on the selected audio unit (built-in loudspeakers, headsets, or handset). Refer to the xStatus Audio SelectedDevice and xCommand Audio Select commands for more information about the selected audio unit.
        '''
    def xCommand_Audio_Volume_Set_Device:_value,_Level:_value():
            pass

        '''
            Set the volume on one of the video conferencing device's audio units (built-in loudspeakers, headsets, or handset) to a specified level. You can use the optional Device parameter to specify which audio unit to address. The most recently selected unit is chosen if you don't specify a unit (see xStatus Audio SelectedDevice). Also refer to xCommand Audio Select.
        '''
    def xCommand_Audio_Volume_SetToDefault_Device:_value():
            pass

        '''
            Set the volume on one of the video conferencing device's audio units (built-in loudspeakers, headsets, or handset) to the default level as defined in the xConfiguration Audio DefaultVolume setting. You can use the optional Device parameter to specify which audio unit to address. The most recently selected unit is chosen if you don't specify a unit (see xStatus Audio SelectedDevice). Also refer to xCommand Audio Select.
        '''
        def ToggleMute():
            pass

        '''
            Toggle the loudspeaker between muted and unmuted.
        '''
        def Unmute():
            pass

        '''
            Set the volume on the device back on after muting.
        '''
    def xCommand_Audio_VuMeter_Start_ConnectorId:_value,_ConnectorType:_value,_IncludePairingQuality:_value,_IntervalMs:_value,_Source:_value():
            pass

        '''
            Start a VU meter to show the audio signal level on the specified connector. Specify both the connector's type and number (ConnectorType, ConnectorId) to uniquely identify the connector. The VU meter measures the input level for frequencies below 20 kHz.
        '''
    def xCommand_Audio_VuMeter_Stop_ConnectorId:_value,_ConnectorType:_value():
            pass

        '''
            Stop the VU meter on the specified connector. You have to specify both the connector's type and number (ConnectorType, ConnectorId) to uniquely identify the connector.
        '''
    class VuMeter:
        pass

        def StopAll():
            pass

        '''
            Stop all VU meters.
        '''
class Bluetooth:
    def __init__(self) -> str:
        pass

class Bookings:
    def __init__(self) -> str:
        pass

    def xCommand_Bookings_Book_BookingRequestUUID:_value,_Duration:_value,_StartTime:_value,_Title:_value():
            pass

        '''
            Book the meeting room for the specified period. If you don’t specify the start time and duration, the room will be booked from now on and for 30 minutes. This command is only available for devices that support the room scheduling feature, refer to the RoomScheduler Enabled setting.
        '''
    def xCommand_Bookings_Clear():
            pass

        '''
            Clear the current stored list of bookings.
        '''
    def xCommand_Bookings_Delete_MeetingId:_value():
            pass

        '''
            Remove the meeting that is identified by the MeetingId parameter. Then the room becomes available for new bookings. This command is only available for devices that support the room scheduling feature, refer to the RoomScheduler Enabled setting.
        '''
    def xCommand_Bookings_Get_Id:_value():
            pass

        '''
            Get the booking information for a specific ID.
        '''
    def xCommand_Bookings_List_DayOffset:_value,_Days:_value,_Limit:_value,_Offset:_value():
            pass

        '''
            List the stored bookings for the device. The list of booking details is received from the management system. All parameters are optional and can be used to limit the search result. If no parameters are set, past, present and future bookings are all listed. To avoid listing bookings from yesterday and before, use DayOffset = 0.
        '''
    def xCommand_Bookings_NotificationSnooze_Id:_value,_SecondsToSnooze:_value():
            pass

        '''
            Sets notifications for the stored bookings in this device to snooze.
        '''
    def xCommand_Bookings_Put_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            This command applies to devices that are either registered to the Webex cloud service or registered to an on-premises service and linked to Webex Edge for Devices. NOTE: This API has special terms and conditions, please refer to the “About the API – Terms and Conditions” section in the API guide. Replace the list of stored bookings. This is a multiline command, with with details of the stored bookings as payload. The meeting information is provided in JSON format. For example: { "Bookings": [ ...
        '''
    def xCommand_Bookings_Respond_MeetingId:_value,_Type:_value():
            pass

        '''
            Accept or decline a meeting invitation. This command applies to devices that are either registered to the Webex cloud service or registered to an on-premises service and linked to Webex Edge for Devices.
        '''
class Call:
    def __init__(self) -> str:
        pass

    def xCommand_Call_Accept_CallId:_value():
            pass

        '''
            Accept an incoming call. If no CallId is specified, all incoming calls are accepted.
        '''
    def xCommand_Call_DTMFSend_CallId:_value,_DTMFString:_value,_Feedback:_value():
            pass

        '''
            Send DTMF tones to the far end.
        '''
    def xCommand_Call_Disconnect_CallId:_value():
            pass

        '''
            Disconnect a call. If no CallId is specified, the currently active call will be disconnected.
        '''
    def xCommand_Call_Forward_DisplayName:_value,_Number:_value():
            pass

        '''
            Specifies what number or URI you want to forward your incoming calls to. The display name is a local reference for the forwarded destination. A message, together with the local reference, is shown on screen when you have configured the device to forward all calls.
        '''
    def xCommand_Call_Hold_CallId:_value,_Reason:_value():
            pass

        '''
            Put a call on hold.
        '''
    def xCommand_Call_Ignore_CallId:_value():
            pass

        '''
            Turns off the ringtone for the incoming call. The call can still be answered.
        '''
    def xCommand_Call_Join_CallId:_value():
            pass

        '''
            Internal usage only.
        '''
    def xCommand_Call_Reject_CallId:_value():
            pass

        '''
            Reject incoming call. If no call id is specified, all incoming calls are rejected.
        '''
    def xCommand_Call_Resume_CallId:_value():
            pass

        '''
            Resume a call that have been put on hold.
        '''
    def xCommand_Call_UnattendedTransfer_CallId:_value,_Number:_value():
            pass

        '''
            Transfers an ongoing call to another participant. Fully supported for SIP calls only.
        '''
    def xCommand_Call_FarEndControl_RequestCapabilities_CallId:_value,_ParticipantId:_value():
            pass

        '''
            Send a request to find out what capabilities a far end camera has for remote control. This command can be issued from a device that is participating in a call and can be used to control the camera of another device within the same call. For on-premises and CMS, this command accesses the camera of the active speaker. For cloud, this command accesses the camera of the specified participant. An additional constraint is that you cannot control the camera of a cloud-based personal mode device. This i...
        '''
    def xCommand_Call_FarEndControl_Camera_Move_CallId:_value,_ParticipantId:_value,_Value:_value():
            pass

        '''
            Move the far end camera (the remote camera). This command can be issued from a device that is participating in a call and can be used to control the camera of another device within the same call. Speakertrack must be disabled on the far end camera. Once the Move command is issued, the far end camera will continue to move in the specified direction until the stop command (ref: xCommand FarEndControl Camera Stop) is issued. For on-premises and CMS, this command accesses the camera of the active sp...
        '''
    def xCommand_Call_FarEndControl_Camera_Stop_CallId:_value,_ParticipantId:_value():
            pass

        '''
            Stop the far end camera after the xCommand FarEndControl Camera Move has been issued. This command can be issued from a device that is participating in a call and can be used to control the camera of another device within the same call. Speakertrack must be disabled on the far end camera. For on-premises and CMS, this command accesses the camera of the active speaker. For cloud, this command accesses the camera of the specified participant. An additional constraint is that you cannot control the...
        '''
    def xCommand_Call_FarEndControl_RoomPreset_Activate_CallId:_value,_ParticipantId:_value,_PresetId:_value():
            pass

        '''
            While in a call, this command is used to activate a preset on the far end device. The preset covers the far end device's camera positions and input video switcher settings. The preset must be stored on the far end device beforehand, either by using the xCommand Preset Store command locally on the far end device, or by using the xCommand FarEndControl Preset Store command from a remote device. Note: The far end device's xConfiguration Conference FarEndControl Mode setting must be switched On for ...
        '''
    def xCommand_Call_FarEndControl_RoomPreset_Store_CallId:_value,_ParticipantId:_value,_PresetId:_value():
            pass

        '''
            While in a call, this command is used to store a preset on the far end device. The preset covers the far end device's camera positions and input video switcher settings. Note: The far end device's xConfiguration Conference FarEndControl Mode setting must be switched On for the FarEndControl commands to work.
        '''
    def xCommand_Call_FarEndControl_Source_Select_CallId:_value,_ParticipantId:_value,_SourceId:_value():
            pass

        '''
            Select which video input source to use as the main source on the far end device. This command can be issued from a device that is participating in a call and can be used to select the source for another device within the same call. For on-premises and CMS, this command selects the source for the active speaker. For cloud, this command selects the source of the specified participant. An additional constraint is that you cannot control the source of a cloud-based personal mode device. This is for ...
        '''
    def xCommand_Call_FarEndMessage_Send_CallId:_value,_Text:_value,_Type:_value():
            pass

        '''
            Send data between two codecs in a point-to-point call, for use with control systems or macros. Works with SIP calls only. Requires that the Conference FarEndMessage Mode is set to On.
        '''
class CallHistory:
    def __init__(self) -> str:
        pass

    def xCommand_CallHistory_AcknowledgeAllMissedCalls():
            pass

        '''
            Turns off the missed calls indicator on the touch controller for all missed calls.
        '''
    def xCommand_CallHistory_AcknowledgeMissedCall_AcknowledgeConsecutiveDuplicates:_value,_CallHistoryId:_value():
            pass

        '''
            Turns off the missed calls indicator on the touch controller for the specified call.
        '''
    def xCommand_CallHistory_DeleteAll_Filter:_value():
            pass

        '''
            Deletes all information on previous calls.
        '''
    def xCommand_CallHistory_DeleteEntry_CallHistoryId:_value,_DeleteConsecutiveDuplicates:_value():
            pass

        '''
            Deletes all information on the specified call.
        '''
    def xCommand_CallHistory_Get_CallHistoryId:_value,_DetailLevel:_value,_Filter:_value,_Limit:_value,_Offset:_value,_SearchString:_value():
            pass

        '''
            Retrieve all information on previous calls made on the device.
        '''
    def xCommand_CallHistory_Recents_DetailLevel:_value,_Filter:_value,_Limit:_value,_Offset:_value,_Order:_value,_SearchString:_value():
            pass

        '''
            Retrieve aggregated information on previous calls made on the device.
        '''
class CallLog:
    def __init__(self) -> str:
        pass

class CallTransfer:
    def __init__(self) -> str:
        pass

class Camera:
    def __init__(self) -> str:
        pass

    def xCommand_Camera_PositionSet_CameraId:_value,_Focus:_value,_Lens:_value,_Pan:_value,_Tilt:_value,_Zoom:_value():
            pass

        '''
            Set the camera position. If the combination of the pan, tilt, zoom, and roll values is not possible, the camera automatically adjusts the values to a valid combination.
        '''
    def xCommand_Camera_Ramp_CameraId:_value,_Focus:_value,_Pan:_value,_PanSpeed:_value,_Tilt:_value,_TiltSpeed:_value,_Zoom:_value,_ZoomSpeed:_value():
            pass

        '''
            Move the camera in a specified direction. The camera moves at specified speed until a stop command is issued. In a daisy chain, you need to know the CameraId for the camera you want to address. Be aware that pan and tilt can be operated simultaneously, but no other combinations. In the latter case only the first operation specified is executed. For example, if you try to run both zoom and pan at the same time, only zoom is executed. NOTE: You must run a stop command to stop the camera, see the e...
        '''
    def xCommand_Camera_Preset_Activate_PresetId:_value():
            pass

        '''
            Activate one of the stored camera presets. This command has no effect on speaker tracking. If speaker tracking is on, it will continue from the preset position. Note that the xCommand Camera Preset commands applies to an individual camera.
        '''
    def xCommand_Camera_Preset_ActivateDefaultPosition_CameraId:_value():
            pass

        '''
            Sets the cameras to their default position, if one is defined. The default position is defined by xCommand Camera Preset Store or by xCommand Camera Preset Edit. Only one default position can be defined per camera. This command has no effect on speaker tracking. If speaker tracking is on, it will continue from the preset position.
        '''
    def xCommand_Camera_Preset_Edit_DefaultPosition:_value,_ListPosition:_value,_Name:_value,_PresetId:_value():
            pass

        '''
            Edit a stored camera preset. You can change the name of the camera preset and its position in the list that is returned by the xCommand Camera Preset List command. You can also change whether or not this preset is the default position for the associated camera. Note that the xCommand Camera Preset commands applies to an individual camera.
        '''
    def xCommand_Camera_Preset_List_CameraId:_value,_DefaultPosition:_value():
            pass

        '''
            List information about available camera presets. Note that the xCommand Camera Preset commands applies to an individual camera.
        '''
    def xCommand_Camera_Preset_Remove_PresetId:_value():
            pass

        '''
            Remove a camera preset. Note that the xCommand Camera Preset commands applies to an individual camera.
        '''
    def xCommand_Camera_Preset_Show_PresetId:_value():
            pass

        '''
            Shows the preset details for the requested PresetId.
        '''
    def xCommand_Camera_Preset_Store_CameraId:_value,_DefaultPosition:_value,_ListPosition:_value,_Name:_value,_PresetId:_value,_TakeSnapshot:_value():
            pass

        '''
            Store the current position (pan and tilt), zoom and focus of the chosen camera. The camera is identified by the CameraId parameter. Note that the xCommand Camera Preset commands applies to an individual camera. The xCommand Camera Preset commands are useful when you want to handle multiple camera positions individually per camera, rather than working with complete sets of camera positions. The individual camera presets are not available for far end control.
        '''
class Cameras:
    def __init__(self) -> str:
        pass

    class SpeakerTrack:
        pass

        def Activate():
            pass

        '''
            Activate SpeakerTrack mode. Requires that xConfiguration Cameras SpeakerTrack Mode is set to Auto (default).
        '''
        def Deactivate():
            pass

        '''
            Deactivate SpeakerTrack mode.
        '''
    def xCommand_Cameras_SpeakerTrack_Diagnostics_Start_Tracking:_value():
            pass

        '''
            Starts diagnostics on the camera's speaker tracking.
        '''
        class Diagnostics:
            pass

            def Stop():
            pass

        '''
            Stops diagnostics on the camera's tracking.
        '''
        class ViewLimits:
            pass

            def Activate():
            pass

        '''
            Start using the limited maximum camera view for speaker tracking (see the Cameras SpeakerTrack ViewLimits StorePosition command). The full camera range is always available for manual camera control.
        '''
            def Deactivate():
            pass

        '''
            Stop using the limited maximum camera view for speaker tracking (see the Cameras SpeakerTrack ViewLimits StorePosition command). The fully zoomed-out camera view will be used instead.
        '''
            def StorePosition():
            pass

        '''
            Store the current camera view as the maximum view (room overview) for speaker tracking. This way you can limit the default maximum view to exclude parts of the room. If you don't set a limit, the maximum view for speaker tracking is the fully zoomed-out camera view.
        '''
    def xCommand_Cameras_SpeakerTrack_Whiteboard_ActivatePosition_CameraId:_value,_WhiteboardId:_value():
            pass

        '''
            Moves the specified camera to the position stored with xCommand Cameras SpeakerTrack Whiteboard StorePosition.
        '''
    def xCommand_Cameras_SpeakerTrack_Whiteboard_SetDistance_Distance:_value,_WhiteboardId:_value():
            pass

        '''
            Set the cameras distance to the whiteboard. This information is needed by the camera to frame the whiteboard automatically.
        '''
    def xCommand_Cameras_SpeakerTrack_Whiteboard_StorePosition_CameraId:_value,_WhiteboardId:_value():
            pass

        '''
            Store the position of the specified camera as the Snap to Whiteboard position. Frame the image so that there is room around the whiteboard for the speaker. To use the Snap to Whiteboard feature it must be enabled with xConfiguration Cameras SpeakerTrack Whiteboard Mode and tracking must be enabled with xConfiguration Cameras SpeakerTrack Mode.
        '''
class Capabilities:
    def __init__(self) -> str:
        pass

class Conference:
    def __init__(self) -> str:
        pass

    def xCommand_Conference_AdmitAll_CallId:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_EndMeeting_CallId:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_HardMute_CallId:_value,_HardMute:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_Lock_CallId:_value,_Lock:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_LowerAllHands_CallId:_value():
            pass

        '''
            Lower the hands of all conference participants.
        '''
    def xCommand_Conference_MuteAll_AudioMute:_value,_CallId:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_MuteOnEntry_CallId:_value,_MuteOnEntry:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_TransferHostAndLeave_CallId:_value():
            pass

        '''
            Lets you leave a meeting you are hosting, but allows the other particpants to continue the meeting. A new host is assigned automatically
        '''
    def xCommand_Conference_Call_AuthenticationResponse_CallId:_value,_ParticipantRole:_value,_Pin:_value():
            pass

        '''
            This command is only available for Cisco Webex registered devices. The command gives a response to an authentication request based on the Conference Call[n] AuthenticationRequest status.
        '''
    def xCommand_Conference_DoNotDisturb_Activate_Timeout:_value():
            pass

        '''
            This command switches on the Do Not Disturb mode, and the Timeout parameter allows you to control when it is switched off again. When Do Not Disturb is switched on, all incoming calls are rejected and registered as missed calls. The calling side receives a busy signal.
        '''
    class DoNotDisturb:
        pass

        def Deactivate():
            pass

        '''
            Switch off the Do Not Disturb mode. When Do Not Disturb is switched off incoming calls come through as normal.
        '''
    def xCommand_Conference_Hand_Lower_CallId:_value():
            pass

        '''
            Lower your hand. Use the raise hand feature to let the host know that you have a question or a comment. Raise Hand is available in meetings with more than two participants. It's not available in meetings started from a Webex space.
        '''
    def xCommand_Conference_Hand_Raise_CallId:_value():
            pass

        '''
            Raise your hand. Use the raise hand feature to let the host know that you have a question or a comment. Raise Hand is available in meetings with more than two participants. It's not available in meetings started from a Webex space.
        '''
    def xCommand_Conference_MeetingAssistant_Start_CallId:_value():
            pass

        '''
            Not applicable in this version.
        '''
    def xCommand_Conference_MeetingAssistant_Stop_CallId:_value():
            pass

        '''
            Not applicable in this version.
        '''
    def xCommand_Conference_Participant_Admit_CallId:_value,_ParticipantId:_value():
            pass

        '''
            Admits or lets in a participant that is waiting to be admitted into the call or meeting. This command is only available Cisco Webex registered devices. A participant is waiting to be admitted if he has status "waiting" in the result from the Conference ParticipantList Search command (*r ParticipantListSearchResult Participant [n] Status = "waiting").
        '''
    def xCommand_Conference_Participant_Disconnect_CallId:_value,_ParticipantId:_value():
            pass

        '''
            Disconnects the participant from a call or meeting. It is only possible to disconnect a participant if the Conference Call[n] Capabilities ParticipantDisconnect status for the meeting shows Available.
        '''
    def xCommand_Conference_Participant_LowerHand_CallId:_value,_ParticipantId:_value():
            pass

        '''
            Lower the hand of a participant in a conference.
        '''
    def xCommand_Conference_Participant_Mute_AudioMute:_value,_CallId:_value,_ParticipantId:_value():
            pass

        '''
            Mutes the participant in the call or meeting. It is only possible to mute a participant if the Conference Call[n] Capabilities ParticipantMute status shows Available.
        '''
    def xCommand_Conference_ParticipantList_Search_CallId:_value,_Limit:_value,_Offset:_value,_SearchString:_value():
            pass

        '''
            Returns details about the participants in the call. The results can be filtered by specifying additional parameters.
        '''
    def xCommand_Conference_Reaction_Disable_CallId:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_Reaction_Enable_CallId:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_Reaction_Send_CallId:_value,_ReactionTone:_value,_ReactionType:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_Reaction_Tone_ReactionTone:_value():
            pass

        '''
            
        '''
    def xCommand_Conference_Recording_Pause_CallId:_value():
            pass

        '''
            Define if the recording of a meeting shall be paused. When you are recording a meeting, you can use this setting if you want to pause the recording. You can resume the recording by using the command Conference Recording Resume.
        '''
    def xCommand_Conference_Recording_Resume_CallId:_value():
            pass

        '''
            Define if the recording of a meeting shall be resumed. When you are recording a meeting, you can use this setting if you want to resume a recording that has previously been paused.
        '''
    def xCommand_Conference_Recording_Start_CallId:_value():
            pass

        '''
            Define if the meeting shall be recorded. Once you are in a meeting, you can use this setting if you want to start recording. Note that the recording commands are only available if your infrastructure (Cisco Meeting Server) supports recording.
        '''
    def xCommand_Conference_Recording_Stop_CallId:_value():
            pass

        '''
            Define if the recording of a meeting shall be stoppped. When you are recording a meeting, you can use this setting to stop recording.
        '''
    class SpeakerLock:
        pass

        def Release():
            pass

        '''
            Releases locked speaker set by xCommand Conference SpeakerLock Set. Default voice switching is switched back on.
        '''
    def xCommand_Conference_SpeakerLock_Set_CallId:_value,_Target:_value():
            pass

        '''
            For manually locking one of the speakers to the prominent speaker position. This overrides the default voice switching.
        '''
class Diagnostics:
    def __init__(self) -> str:
        pass

    def xCommand_Diagnostics_Run_ResultSet:_value():
            pass

        '''
            This command runs self-diagnostics commands on the device.
        '''
class FacilityService:
    def __init__(self) -> str:
        pass

class FarEndMessage:
    def __init__(self) -> str:
        pass

class FeccReceive:
    def __init__(self) -> str:
        pass

class Files:
    def __init__(self) -> str:
        pass

class H320:
    def __init__(self) -> str:
        pass

class H323:
    def __init__(self) -> str:
        pass

class HttpClient:
    def __init__(self) -> str:
        pass

    def xCommand_HttpClient_Delete_AllowInsecureHTTPS:_value,_Header:_value,_ResponseSizeLimit:_value,_ResultBody:_value,_Timeout:_value,_Url:_value():
            pass

        '''
            Sends an HTTP(S) Delete request to the server that is specified in the Url parameter. You can use the AllowInsecureHTTPS parameter to specify whether or not to validate the server's certificate before sending data over HTTPS. This parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS is set to On. The command returns the HTTP status code along with the data returned from the server (HTTP headers and body).
        '''
    def xCommand_HttpClient_Get_AllowInsecureHTTPS:_value,_Header:_value,_ResponseSizeLimit:_value,_ResultBody:_value,_Timeout:_value,_Url:_value():
            pass

        '''
            Sends an HTTP(S) Get request to the server that is specified in the Url parameter. You can use the AllowInsecureHTTPS parameter to specify whether or not to validate the server's certificate before sending data over HTTPS. This parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS is set to On. The command returns the HTTP status code along with the data returned from the server (HTTP headers and body).
        '''
    def xCommand_HttpClient_Patch_AllowInsecureHTTPS:_value,_Header:_value,_ResponseSizeLimit:_value,_ResultBody:_value,_Timeout:_value,_Url:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Sends an HTTP(S) Patch request to the server that is specified in the Url parameter. This is a multiline command, so the payload (data) follows after the parameters. You can use the AllowInsecureHTTPS parameter to specify whether or not to validate the server's certificate before sending data over HTTPS. This parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS is set to On. The command returns the HTTP status code along with the data returned from the server (HTTP hea...
        '''
    def xCommand_HttpClient_Post_AllowInsecureHTTPS:_value,_Header:_value,_ResponseSizeLimit:_value,_ResultBody:_value,_Timeout:_value,_Url:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Sends an HTTP(S) Post request to the server that is specified in the Url parameter. You can use the AllowInsecureHTTPS parameter to specify whether or not to validate the server's certificate before sending data over HTTPS. This parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS is set to On. This is a multiline command, so the payload (data) follows after the parameters.
        '''
    def xCommand_HttpClient_Put_AllowInsecureHTTPS:_value,_Header:_value,_ResponseSizeLimit:_value,_ResultBody:_value,_Timeout:_value,_Url:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Sends an HTTP(S) Put request to the server that is specified in the Url parameter. You can use the AllowInsecureHTTPS parameter to specify whether or not to validate the server's certificate before sending data over HTTPS. This parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS is set to On. This is a multiline command, so the payload (data) follows after the parameters.
        '''
    def xCommand_HttpClient_Allow_Hostname_Add_Expression:_value():
            pass

        '''
            Adds an HTTP(S) server to the list of allowed servers (hosts). The HttpClient Allow Hostname commands let you set up and maintain a list of up to ten allowed hosts. As long as the list is not empty, you can send HTTP(S) requests only to the servers in the list. The check against the list is performed both when using insecure (HTTP) and secure (HTTPS) transfer of data.
        '''
        class Hostname:
            pass

            def Clear():
            pass

        '''
            Removes all HTTP(S) servers from the list of allowed servers (hosts), leaving you with an empty list.
        '''
            def List():
            pass

        '''
            Returns the list of allowed HTTP(S) servers (hosts). The HttpClient Allow Hostname commands let you set up and maintain a list of up to ten allowed hosts. As long as the list is not empty, you can send HTTP(S) requests only to the servers in the list. The check against the list is performed both when using insecure (HTTP) and secure (HTTPS) transfer of data.
        '''
    def xCommand_HttpClient_Allow_Hostname_Remove_Id:_value():
            pass

        '''
            Removes an HTTP(S) server from the list of allowed servers (hosts). Use the HttpClient Allow Hostname List command to find the indentifier of each entry in the list.
        '''
class HttpFeedback:
    def __init__(self) -> str:
        pass

    def xCommand_HttpFeedback_Deregister_FeedbackSlot:_value():
            pass

        '''
            Deregister the HTTP feedback over HTTP(S).
        '''
    def xCommand_HttpFeedback_Enable_FeedbackSlot:_value():
            pass

        '''
            Re-enables a previously registered feedback slot after it has failed and become deactivated.
        '''
    def xCommand_HttpFeedback_Register_Expression:_value,_FeedbackSlot:_value,_Format:_value,_ServerUrl:_value():
            pass

        '''
            Register the device to an HTTP(S) server to return XML feedback over HTTP(S) to specific URLs.
        '''
class ICE:
    def __init__(self) -> str:
        pass

class Logging:
    def __init__(self) -> str:
        pass

    def xCommand_Logging_SendLogs():
            pass

        '''
            Send logs to the Cisco Webex cloud. These logs can help diagnose and fix issues with the device. The command returns a log ID, which an administrator or TAC engineer can use to identify and download the logs. For the command to work, the device must either be registered to the Webex cloud service or registered to an on-premises service and linked to Webex Edge for Devices. Additionally, for devices linked to Webex Edge for Devices, the xConfiguration Logging CloudUpload Mode must be set to On.
        '''
    def xCommand_Logging_ExtendedLogging_Start_Duration:_value,_PacketDump:_value,_PacketDumpRotateSize:_value,_RenderingDump:_value():
            pass

        '''
            Start running continuous extended logging for the specified duration.
        '''
    def xCommand_Logging_ExtendedLogging_Stop_RemovePacketDump:_value,_RemoveRenderingDump:_value():
            pass

        '''
            Stop running the extended logging process.
        '''
class Macros:
    def __init__(self) -> str:
        pass

    class Log:
        pass

        def Clear():
            pass

        '''
            Clears the Macros Logs.
        '''
    def xCommand_Macros_Log_Get_Offset:_value():
            pass

        '''
            Shows the logs for all running macros and for the runtime itself.
        '''
    def xCommand_Macros_Macro_Activate_Name:_value():
            pass

        '''
            Activates a macro created on this device.
        '''
    def xCommand_Macros_Macro_Deactivate_Name:_value():
            pass

        '''
            Deactivates a macro currently running on this device.
        '''
    def xCommand_Macros_Macro_Get_Content:_value,_Name:_value():
            pass

        '''
            Shows the details of a macro created on this device.
        '''
    def xCommand_Macros_Macro_Remove_Name:_value():
            pass

        '''
            Removes a macro created on this device.
        '''
    class Macro:
        pass

        def RemoveAll():
            pass

        '''
            Removes all of the macros created on this device.
        '''
    def xCommand_Macros_Macro_Rename_Name:_value,_NewName:_value,_Overwrite:_value():
            pass

        '''
            Renames a macro created on this device.
        '''
    def xCommand_Macros_Macro_Save_Name:_value,_Overwrite:_value,_Transpile:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Saves the details of a macro. This is a multiline command.
        '''
    def xCommand_Macros_Macro_Roles_Set_Name:_value,_Role:_value():
            pass

        '''
            Sets the role for a macro.
        '''
    class Runtime:
        pass

        def Restart():
            pass

        '''
            Restarts all of the macros set up on this device.
        '''
        def Start():
            pass

        '''
            Starts all of the macros set up on this device.
        '''
        def Status():
            pass

        '''
            Shows the current status of the macros runtime on this device.
        '''
        def Stop():
            pass

        '''
            Stops all of the macros set up on this device.
        '''
class MediaChannels:
    def __init__(self) -> str:
        pass

class Message:
    def __init__(self) -> str:
        pass

    def xCommand_Message_Send_Text:_value():
            pass

        '''
            Triggers a Message Send event which sends text to any listening clients.
        '''
class Network:
    def __init__(self) -> str:
        pass

    def xCommand_Network_SNMP_USM_User_Add_AuthenticationPassword:_value,_AuthenticationProtocol:_value,_Name:_value,_PrivacyPassword:_value():
            pass

        '''
            
        '''
    def xCommand_Network_SNMP_USM_User_Delete_Name:_value():
            pass

        '''
            
        '''
    def xCommand_Network_SNMP_USM_User_List():
            pass

        '''
            
        '''
    def xCommand_Network_Wifi_Configure_AllowMissingCA:_value,_AnonymousIdentity:_value,_Identity:_value,_Password:_value,_SSID:_value,_Type:_value():
            pass

        '''
            Configures the device to be able to connect to a specific Wi-Fi network. This is only available if Wi-Fi is enabled on the device. You must unplug the Ethernet cable before you can connect to Wi-Fi. Both WPA2-only and mixed mode access points with WPA2 are supported.
        '''
    def xCommand_Network_Wifi_Delete_SSID:_value():
            pass

        '''
            Deletes the specified Wi-Fi network connection from the device. This command is only available if Wi-Fi services are turned on and ethernet is disconnected.
        '''
    class Wifi:
        pass

        def List():
            pass

        '''
            Lists the details of the current Wi-Fi connection. This command is only available if Wi-Fi services are turned on and ethernet is disconnected.
        '''
    def xCommand_Network_Wifi_Scan_Start_Duration:_value():
            pass

        '''
            Scans for available Wi-Fi networks.
        '''
        class Scan:
            pass

            def Stop():
            pass

        '''
            Stops an ongoing Wi-Fi scan.
        '''
class NetworkServices:
    def __init__(self) -> str:
        pass

class Peripherals:
    def __init__(self) -> str:
        pass

    def xCommand_Peripherals_Connect_HardwareInfo:_value,_ID:_value,_Name:_value,_NetworkAddress:_value,_SerialNumber:_value,_SoftwareInfo:_value,_Type:_value():
            pass

        '''
            Register peripherals that are connected to the device, such as control systems and touch panels. The registered peripherals are displayed on the web interface under Configuration > Peripherals. This command should be used when the peripheral connects to the codec for the first time or when the software version on the peripheral has changed. The list of connected devices is available with the command xStatus Peripherals ConnectedDevice [n] Status.
        '''
    def xCommand_Peripherals_HeartBeat_ID:_value,_Timeout:_value():
            pass

        '''
            When a peripheral is registered as a connected device, you can set it to send a heartbeat to the codec to let the codec know that it is still connected. This will keep the device on the xStatus Peripherals ConnectedDevice list. If the peripheral is not set to send a heartbeat, the device will disappear from the list after a while. Note: Does not apply to cameras.
        '''
    def xCommand_Peripherals_List_Connected:_value,_Type:_value():
            pass

        '''
            Lists all currently and previously connected peripherals.
        '''
    def xCommand_Peripherals_Purge_ID:_value():
            pass

        '''
            Force unpair a video conferencing device from an ISDN Link when a connection has been lost. Note: You must also unpair the ISDN Link to be able to pair it to another video conferencing device.
        '''
    def xCommand_Peripherals_Pairing_Pair_MacAddress:_value():
            pass

        '''
            Pair an ISDN Link to a video conferencing device.
        '''
    def xCommand_Peripherals_Pairing_Unpair_MacAddress:_value():
            pass

        '''
            Unpair the video conferencing device from an ISDN Link, when the two have contact.
        '''
    def xCommand_Peripherals_Pairing_DeviceDiscovery_Start_AutoPairing:_value,_DeviceType:_value,_Timeout:_value():
            pass

        '''
            Start device discovery to detect ISDN Links in the same network.
        '''
    def xCommand_Peripherals_Pairing_PinPairing_Start_Duration:_value,_PinVisibleOnScreen:_value,_Retries:_value():
            pass

        '''
            When connecting a touch controller to a video device across the network, you can pair by using a PIN or a passphrase. To initiate pairing by PIN, issue this command.
        '''
        class PinPairing:
            pass

            def Stop():
            pass

        '''
            Stop the pin pairing process.
        '''
    def xCommand_Peripherals_TouchPanel_Configure_ID:_value,_Location:_value,_Mode:_value():
            pass

        '''
            
        '''
class Phonebook:
    def __init__(self) -> str:
        pass

    def xCommand_Phonebook_Search_ContactMethodLimit:_value,_ContactType:_value,_FolderId:_value,_Limit:_value,_Offset:_value,_PhonebookId:_value,_PhonebookType:_value,_Recursive:_value,_SearchField:_value,_SearchFilter:_value,_SearchString:_value,_Tag:_value():
            pass

        '''
            The search command lets you search in both the local and corporate phone books. A search gives a ResultSet. The total number of folders and contacts (TotalRows) is always included in the result set when searching the local phone book. When searching a corporate phonebook the total number of folders and contacts may not be included. Whether it is included or not depends on the backend corporate phonebook service (e.g. CUCM, VCS, TMS) and its version.
        '''
    def xCommand_Phonebook_Contact_Add_CallRate:_value,_CallType:_value,_Device:_value,_FolderId:_value,_ImageURL:_value,_Name:_value,_Number:_value,_Protocol:_value,_Tag:_value,_Title:_value():
            pass

        '''
            Add a new contact to the local phonebook. The command returns the ContactId, which is a unique string that identifies the contact; typically, the format is “localContactId-n”. You can add several contact methods to a contact using the xCommand Phonebook ContactMethod Add command. Note that only the first contact method will appear in the Favorites list on the touch controller. All contact methods are available on the other UIs.
        '''
    def xCommand_Phonebook_Contact_Delete_ContactId:_value():
            pass

        '''
            Delete an existing contact from the local phonebook.
        '''
    def xCommand_Phonebook_Contact_Modify_ContactId:_value,_FolderId:_value,_ImageURL:_value,_Name:_value,_Tag:_value,_Title:_value():
            pass

        '''
            Modify contact details of an existing contact in the local phonebook. The following parameters can be changed using this command: Name, FolderId, ImageURL and Title. You must use the xCommand Phonebook ContactMethod Modify command to change the other parameters: Number, Protocol, CallRate, CallType and Device.
        '''
    def xCommand_Phonebook_ContactMethod_Add_CallRate:_value,_CallType:_value,_ContactId:_value,_Device:_value,_Number:_value,_Protocol:_value():
            pass

        '''
            Add contact details for an existing contact in the local phonebook. The command returns the ContactMethodId, which is a unique string that identifies the contact method; typically, the format is “n”. You can add several contact methods to a contact. Note that only the first contact method will appear in the Favorites list on the device's user interface. The first contact method may have been created when issuing the xCommand Phonebook Contact Add command to make the contact. All contact methods ...
        '''
    def xCommand_Phonebook_ContactMethod_Delete_ContactId:_value,_ContactMethodId:_value():
            pass

        '''
            Delete a contact method from an existing contact in the local phonebook.
        '''
    def xCommand_Phonebook_ContactMethod_Modify_CallRate:_value,_CallType:_value,_ContactId:_value,_ContactMethodId:_value,_Device:_value,_Number:_value,_Protocol:_value():
            pass

        '''
            Modify details about the contact method for an existing contact in the local phonebook.
        '''
    def xCommand_Phonebook_Folder_Add_Name:_value,_ParentFolderId:_value():
            pass

        '''
            Phonebook entries can be stored in folders. Use this command to add a folder to the local phonebook. The command returns the FolderId, which is a unique string that identifies the folder; typically, the format is “localGroupId-n”.
        '''
    def xCommand_Phonebook_Folder_Delete_FolderId:_value():
            pass

        '''
            Delete an existing folder from the local phonebook.
        '''
    def xCommand_Phonebook_Folder_Modify_FolderId:_value,_Name:_value,_ParentFolderId:_value():
            pass

        '''
            Modify an existing phonebook folder.
        '''
class Presentation:
    def __init__(self) -> str:
        pass

    def xCommand_Presentation_Start_ConnectorId:_value,_Instance:_value,_Layout:_value,_PresentationSource:_value,_SendingMode:_value():
            pass

        '''
            Open a media stream from the selected presentation source. You can combine multiple presentation sources in a single presentation video stream (the maximum number of different input sources depend on the type of video conferencing device) by adding multiple ConnectorId or PresentationSource parameters in the same command. The order in which you place them in the command determines the order in which the sources show up on the screen. You cannot use a mix of identifier types in the same command; ...
        '''
    def xCommand_Presentation_Stop_Instance:_value,_PresentationSource:_value():
            pass

        '''
            Stop the media stream from the presentation source.
        '''
class Provisioning:
    def __init__(self) -> str:
        pass

    def xCommand_Provisioning_CompleteUpgrade():
            pass

        '''
            Starts installing the software upgrade if you wish to install it before it is set to do so.
        '''
    def xCommand_Provisioning_PostponeUpgrade_Reason:_value,_SecondsToPostpone:_value():
            pass

        '''
            Postpones the installing of the software upgrade.
        '''
    def xCommand_Provisioning_CUCM_ExtensionMobility_Login_Pin:_value,_Profile:_value,_UserId:_value():
            pass

        '''
            Login command for the Extension Mobility service. You log in to the Extension Mobility service with a username (UserId) and pin code (Pin). The username and pin code are set up in CUCM. CUCM also supports multiple profiles for a user. If you, for a user that has multiple profiles, submit a login command with only username and pin code, CUCM will send a list of available profiles back to the device. Then the device will create corresponding ExtensionMobilityProfileSelection Profile events, so tha...
        '''
        class ExtensionMobility:
            pass

            def Logout():
            pass

        '''
            This command will log you out of your Extension Mobility profile.
        '''
    def xCommand_Provisioning_Service_Fetch_Checksum:_value,_ChecksumType:_value,_Mode:_value,_Origin:_value,_URL:_value():
            pass

        '''
            Add or update the customization template that details the custom elements of the device. Examples of custom elements are: branding images, macros, favorites, sign-in banner, and in-room control panels.
        '''
class Proximity:
    def __init__(self) -> str:
        pass

    class Services:
        pass

        def Activate():
            pass

        '''
            Reactivate the Proximity services that were deactivated with xCommand Proximity Services Deactivate.
        '''
        def Deactivate():
            pass

        '''
            This command deactivates all proximity services on the device. To reactivate proximity services use the command xCommand Proximity Services Activate.
        '''
class RoomAnalytics:
    def __init__(self) -> str:
        pass

class RoomCleanup:
    def __init__(self) -> str:
        pass

    def xCommand_RoomCleanup_Cancel():
            pass

        '''
            Cancel the scheduled daily room cleanup.
        '''
    def xCommand_RoomCleanup_Run_ContentType:_value,_Delay:_value():
            pass

        '''
            Run a cleanup of the specified type of data, as applicable.
        '''
class RoomPreset:
    def __init__(self) -> str:
        pass

    def xCommand_RoomPreset_Activate_PresetId:_value():
            pass

        '''
            Activate one of the locally stored presets. Note that information about all video input sources, and pan, tilt, zoom and focus values for all cameras are included in the same preset. In contrast, the xCommand Camera Preset commands applies to individual cameras only.
        '''
    def xCommand_RoomPreset_Clear_PresetId:_value():
            pass

        '''
            Delete a preset. Note that information about all video input sources, and pan, tilt, zoom and focus values for all cameras are included in the same preset. In contrast, the xCommand Camera Preset commands applies to individual cameras only.
        '''
    def xCommand_RoomPreset_Store_Description:_value,_PresetId:_value,_Type:_value():
            pass

        '''
            Store the connector selections for all video input sources and the current position (pan and tilt), zoom and focus values for all cameras. Note that information about all video input sources, and pan, tilt, zoom and focus values for all cameras are included in the same preset. The device may hold 15 such predefined video input presets. These presets are available for far end control, i.e. they are referred in the PresetId parameter of the xCommand FarEndControl Preset Activate command. In contra...
        '''
class RoomReset:
    def __init__(self) -> str:
        pass

class RoomScheduler:
    def __init__(self) -> str:
        pass

class SIP:
    def __init__(self) -> str:
        pass

class Security:
    def __init__(self) -> str:
        pass

    def xCommand_Security_Persistency_CallHistory:_value,_Configurations:_value,_ConfirmAndReboot:_value,_DHCP:_value,_InternalLogging:_value,_LocalPhonebook:_value():
            pass

        '''
            Set the following features to persistent or non-persistent mode. In non-persistent mode the information gathered by the specified feature does not persist a reboot of the device. Persistent mode is the default. This command reboots the device.
        '''
    def xCommand_Security_Certificates_CA_Add_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Uploads CA security certificates to this device. This is a multiline command.
        '''
    def xCommand_Security_Certificates_CA_Delete_Fingerprint:_value():
            pass

        '''
            Deletes a CA security certificate from this device.
        '''
    def xCommand_Security_Certificates_CA_Show_Format:_value():
            pass

        '''
            Shows the details for the CA security certificates on this device.
        '''
    def xCommand_Security_Certificates_CUCM_CTL_Delete():
            pass

        '''
            api-description all="true">Deletes the Certificate Trust List (CTL) and Identity Trust List (ITL) from this device. This command applies only to devices that are registered to CUCM.
        '''
    def xCommand_Security_Certificates_CUCM_CTL_Show():
            pass

        '''
            Shows the details of the Certificate Trust List (CTL) on this device. CTL is used for devices that are registered to CUCM and contains a list of certificates for services within the CUCM cluster that the device is to trust.
        '''
    def xCommand_Security_Certificates_CUCM_ITL_Show():
            pass

        '''
            Shows the details of the Identity Trust List (ITL) on this device. ITL is used for devices that are registered to CUCM and contains a list of certificates for services within the CUCM cluster that the device is to trust.
        '''
    def xCommand_Security_Certificates_CUCM_MIC_Show_Format:_value():
            pass

        '''
            Shows the details of the Manufacture Installed Certificate (MIC) on this device. A MIC is signed by the Cisco Manufacturing CA and is installed on the device during production. This certificate is immutable.
        '''
    def xCommand_Security_Certificates_Services_Activate_Fingerprint:_value,_Purpose:_value():
            pass

        '''
            Activates a security certificate on this device.
        '''
    def xCommand_Security_Certificates_Services_Add_PrivateKeyPassword:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Uploads security certificates to this device. This is a multiline command.
        '''
    def xCommand_Security_Certificates_Services_Deactivate_Fingerprint:_value,_Purpose:_value():
            pass

        '''
            Deactivates security certificates on this device.
        '''
    def xCommand_Security_Certificates_Services_Delete_Fingerprint:_value():
            pass

        '''
            Deletes security certificates from this device.
        '''
    def xCommand_Security_Certificates_Services_Show_Filter:_value,_FingerprintAlgorithm:_value,_Format:_value():
            pass

        '''
            Shows details for security certificates on this device.
        '''
    def xCommand_Security_Certificates_ThirdParty_Disable_Fingerprint:_value():
            pass

        '''
            Disables a bundled certificate used for SMTP and HttpClient. Disabling a certificate results in a server providing a certificate signed with this root certificate will be declined.
        '''
    def xCommand_Security_Certificates_ThirdParty_Enable_Fingerprint:_value():
            pass

        '''
            Enables a bundled certificate used for SMTP and HttpClient.
        '''
        class ThirdParty:
            pass

            def List():
            pass

        '''
            Lists all bundled certificates and their state.
        '''
    def xCommand_Security_Certificates_ThirdParty_Show_Fingerprint:_value,_Format:_value():
            pass

        '''
            Shows a single third-party certificate.
        '''
    def xCommand_Security_Certificates_Webex_Show_Filter:_value,_Format:_value():
            pass

        '''
            This command applies only to devices that are registered to the Cisco Webex cloud service. Shows the list of trusted CA certificates that verifies the certificates of servers and services used by the Cisco Webex cloud.
        '''
    def xCommand_Security_Certificates_WebexIdentity_Show_Filter:_value,_Format:_value():
            pass

        '''
            This command applies only to devices that are registered to the Cisco Webex cloud service. Shows the root Certificate Authority (CA) list for Webex Identity.
        '''
    class Ciphers:
        pass

        def List():
            pass

        '''
            List the ciphers supported by various services (domains). Result: Name: Name of this domain. * Syslog-TLS: Used for logging over TLS. * HTTPS server: Used by the endpoint's own web server. * HTTPS client: Used for all https client traffic from the endpoint. * Pairing: Used for peripheral pairing to touch devices and microphones/amplifiers. * SIP TLS: Used for direct IP SIP connections, SIP connections to CUCM or to VCS or other SIP proxies when transport is TLS. Cipherlist: The actual ...
        '''
    def xCommand_Security_ClientSecret_Populate_Secret:_value():
            pass

        '''
            This command applies only to devices that are registered to the Cisco Webex cloud service. Accepts a base64url encoded plain text value for seeding the client secret on the device for the first time. To update the secret after that first time, you must supply a JWE blob containing the new secret encrypted by the old secret. This is a multiline command.
        '''
    class Session:
        pass

        def Get():
            pass

        '''
            Shows details of your current session.
        '''
        def List():
            pass

        '''
            List active sessions.
        '''
    def xCommand_Security_Session_Terminate_SessionId:_value():
            pass

        '''
            Terminate a session.
        '''
class SerialPort:
    def __init__(self) -> str:
        pass

class Standby:
    def __init__(self) -> str:
        pass

    def xCommand_Standby_Activate():
            pass

        '''
            Set the device in standby mode, which turns off the video outputs and put the camera into sleep mode.
        '''
    def xCommand_Standby_Deactivate():
            pass

        '''
            Bring the device out of standby mode.
        '''
    def xCommand_Standby_Halfwake():
            pass

        '''
            Sets the device to "Halfwake" state. This state informs the user from the UI, to pick up a remote or to tap the touch device to get started.
        '''
    def xCommand_Standby_ResetHalfwakeTimer_Delay:_value():
            pass

        '''
            Sets a temporary Halfwake timer delay. If the device is in Halfwake mode when the reset timer is set, the device is brought out of Halfwake mode. When left idle for the given delay the device goes into halfwake mode.
        '''
    def xCommand_Standby_ResetTimer_Delay:_value():
            pass

        '''
            Reset the standby delay timer or set a temporary standby delay. If the device is in standby mode when the timer is set, the device is brought out of standby mode before starting the countdown. If you don't specify a Delay, the standby delay timer is reset, and the device goes into standby after the period that is given by the Standby Delay setting (xConfiguration Standby Delay). If you do specify a Delay, the device goes into standby when it has been idle for the specified period. Next time, the...
        '''
class SystemUnit:
    def __init__(self) -> str:
        pass

    def xCommand_SystemUnit_Boot_Action:_value,_Force:_value():
            pass

        '''
            Reboot the device.
        '''
    def xCommand_SystemUnit_FactoryReset_Confirm:_value,_Keep:_value,_TrailingAction:_value():
            pass

        '''
            Reset the codec to factory default settings. The call logs are deleted and all device parameters are reset to default values. All files that have been uploaded to the codec are deleted. Option key(s) are not affected. Use the parameter Keep in order to choose which configurations and files to keep when you factory reset the device. As a default the device restarts after the factory reset, but other behaviors can be forced by selecting a different TrailingAction.
        '''
    def xCommand_SystemUnit_SoftReset_Confirm:_value():
            pass

        '''
            Reset most parameters to their default values. This does not include parameters associated with room setup, such as camera position, language, and volume.
        '''
    def xCommand_SystemUnit_SoftwareUpgrade_Forced:_value,_URL:_value():
            pass

        '''
            Initiate a software upgrade by fetching the software from a given URL.
        '''
    class DeveloperPreview:
        pass

        def Activate():
            pass

        '''
            Activate developer preview mode. When developer preview mode is activated and you have a DeveloperPreview option key installed, you will get access to public-api-preview xAPI nodes.
        '''
        def Deactivate():
            pass

        '''
            Deactivate developer preview mode.
        '''
    class FirstTimeWizard:
        pass

        def Stop():
            pass

        '''
            Stops the wizard which appears the first time you start the device, so the device can be set up without it. The wizard only appears again if the device is reset to its factory default settings.
        '''
    class Notifications:
        pass

        def RemoveAll():
            pass

        '''
            Clears the list of system notifications that are reported by xStatus SystemUnit Notifications Text/Type.
        '''
    def xCommand_SystemUnit_OptionKey_Add_Key:_value():
            pass

        '''
            Add an option key to support additional features.
        '''
    class OptionKey:
        pass

        def List():
            pass

        '''
            List all option keys.
        '''
    def xCommand_SystemUnit_OptionKey_Remove_Type:_value():
            pass

        '''
            Remove a specified option key.
        '''
    def xCommand_SystemUnit_OptionKey_RemoveAll_Confirm:_value():
            pass

        '''
            Remove all option keys.
        '''
    class SignInBanner:
        pass

        def Clear():
            pass

        '''
            Clear the sign in banner set with xCommand SystemUnit SignInBanner Set.
        '''
        def Get():
            pass

        '''
            Get the custom message set with xCommand SystemUnit SignInBanner Set.
        '''
    def xCommand_SystemUnit_SignInBanner_Set_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Set a sign in banner with a custom message on the device's user interface. This is a multiline command. Use: xCommand SystemUnit SignInBanner Set <enter> Banner text <enter> . <enter>
        '''
    class WelcomeBanner:
        pass

        def Clear():
            pass

        '''
            Clear the welcome banner set with xCommand SystemUnit WelcomeBanner Set.
        '''
        def Get():
            pass

        '''
            Get the custom message set with xCommand SystemUnit WelcomeBanner Set.
        '''
    def xCommand_SystemUnit_WelcomeBanner_Set_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Set up a welcome banner that the user sees after they sign in to the device's web interface or the command line interface. The banner can for example contain information that the user needs to get started or things they need to be aware of when changing settings. This is a multiline command. Use: xCommand SystemUnit WelcomeBanner Set <enter> Banner text <enter> . <enter>
        '''
class Time:
    def __init__(self) -> str:
        pass

    class DateTime:
        pass

        def Get():
            pass

        '''
            Read the time and date from the device.
        '''
    def xCommand_Time_DateTime_Set_Day:_value,_Hour:_value,_Minute:_value,_Month:_value,_Second:_value,_Year:_value():
            pass

        '''
            Set the date and time for the device, if not available from NTP (Network Time Protocol).
        '''
class UserInterface:
    def __init__(self) -> str:
        pass

    class Branding:
        pass

        def Clear():
            pass

        '''
            Deletes the custom wallpaper, the brand background image, and the logo files from the device.
        '''
    def xCommand_UserInterface_Branding_Delete_Type:_value():
            pass

        '''
            Deletes the image file, which is specified in the Type parameter, from the device.
        '''
    def xCommand_UserInterface_Branding_Fetch_Checksum:_value,_ChecksumType:_value,_CustomId:_value,_Type:_value,_URL:_value():
            pass

        '''
            Fetches an image file from a URL and stores the file on the device. Supply the URL first. The following image formats are supported: BMP, GIF, JPEG, and PNG. The maximum image size is 16 megapixels, and the maximum file size is 8 MB. The Type parameter determines what kind of image it is. If it is a background image, the associated feature (Custom wallpaper or Branding with background and logo) is automatically applied. This command issues an HTTP request, so it is included in the HTTP requests ...
        '''
    def xCommand_UserInterface_Branding_Get_Size:_value,_Type:_value():
            pass

        '''
            The command returns the image file that is specified in the Type parameter, given that such a file is stored on the device. The file is Base64 encoded. The format is JPG for background images and PNG for logos, regardless of the format of the originally uploaded file. Background images are stored in three sizes, one for the main screen, one for the touch controller, and one for the web interface illustrations. Use the Size parameter to choose which one to get. Logos have only one size.
        '''
    def xCommand_UserInterface_Branding_Updated_Type:_value():
            pass

        '''
            This command creates an event that tells that a new image file is uploaded to the device and ready for use. The Type parameter identifies what kind of image it is.
        '''
    def xCommand_UserInterface_Branding_Upload_CustomId:_value,_Type:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Uploads an image file to the device. The following image formats are supported: BMP, GIF, JPEG, and PNG, and the maximum image size is 16 megapixels. The file must be Base64 encoded, and the maximum file size is 4 MByte. The Type parameter specifies the usage of the image. If it is a background image, the associated feature (Custom wallpaper or Branding with background and logo) is automatically applied. This is a multiline command.
        '''
    def xCommand_UserInterface_Extensions_Clear_ActivityType:_value():
            pass

        '''
            Delete user interface extensions (custom buttons, panels, and widgets) from the device. If you don't specify an ActivityType, all extensions are deleted.
        '''
    def xCommand_UserInterface_Extensions_Export_EmbedData:_value():
            pass

        '''
            Export the UserInterface Extensions as the XML result of this command. This gives the same result as extracting through the local web interface, but it can be used programmatically.
        '''
    def xCommand_UserInterface_Extensions_List_ActivityType:_value():
            pass

        '''
            List user interface extensions (custom buttons, panels, and widgets) that exist on the device. If you don't specify an ActivityType, all extensions are listed.
        '''
    def xCommand_UserInterface_Extensions_Set_ConfigId:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Set the configuration scheme you have chosen in the user interface extensions (widgets) for your device. Updates the UserInterface Extensions status tree. This is a multiline command.
        '''
    def xCommand_UserInterface_Extensions_Icon_Delete_Id:_value():
            pass

        '''
            Delete an icon from the device's list of UI extension icons. Specify the id of the icon to be deleted. You can use xCommand UserInterface Extensions Icon List to get a list of all the icons with ids. If you are not sure which icon is the one you are looking for, you can use xcommand UserInterface Icon Get to get the base64-encoded value and use an internet tool to decode base64 to image.
        '''
    def xCommand_UserInterface_Extensions_Icon_DeleteAll_Filter:_value():
            pass

        '''
            Delete all or a subset of UI extensions icons.
        '''
    def xCommand_UserInterface_Extensions_Icon_Download_Url:_value():
            pass

        '''
            Download an icon from the specified URL and save it as a UI Extensions icon on the device.
        '''
    def xCommand_UserInterface_Extensions_Icon_Fetch_Url:_value():
            pass

        '''
            Search a website for a representative icon and download this to the device for use with web apps and other UI extensions.
        '''
    def xCommand_UserInterface_Extensions_Icon_Get_Id:_value():
            pass

        '''
            Get a base64-encoded representation of the UI Extensions icon with the specified Id. If you want to see the image, you can use an internet tool to decode base64 to image. Use xCommand UserInterface Extensions Icon List to get a list of all the icon Ids.
        '''
        class Icon:
            pass

            def List():
            pass

        '''
            Get a list of the unique identifiers for all the UI extension icons on the device.
        '''
    def xCommand_UserInterface_Extensions_Icon_Upload_Id:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Upload an icon image for use by UI extensions on the device. This is a multiline command. Provide a base64-encoded version of an image.
        '''
    def xCommand_UserInterface_Extensions_Panel_Clicked_PanelId:_value():
            pass

        '''
            Creates an event when the user clicks a custom panel.
        '''
        class Panel:
            pass

            def Close():
            pass

        '''
            Closes an open custom panel.
        '''
    def xCommand_UserInterface_Extensions_Panel_Open_PageId:_value,_PanelId:_value():
            pass

        '''
            Opens the custom panel that has the given PanelId. If the panel has multiple pages you can specify which page to open by including the PageId parameter.
        '''
    def xCommand_UserInterface_Extensions_Panel_Remove_PanelId:_value():
            pass

        '''
            Removes the custom panel from the user interface of this device.
        '''
    def xCommand_UserInterface_Extensions_Panel_Save_PanelId:_value_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Adds a custom panel to the current configuration. The panel will be added to the configuration, but if a panel with the same panel ID already exists, it will be overwritten. This is a multiline command.
        '''
    def xCommand_UserInterface_Extensions_Panel_Update_Color:_value,_Icon:_value,_IconId:_value,_Name:_value,_PanelId:_value,_Visibility:_value():
            pass

        '''
            Updates the custom panel that has the given PanelId. Successful changes are immediately visible on the endpoint.
        '''
    def xCommand_UserInterface_Extensions_Widget_Action_Type:_value,_Value:_value,_WidgetId:_value():
            pass

        '''
            Sets the action of the given widget. Updates the UserInterface Extensions status tree.
        '''
    def xCommand_UserInterface_Extensions_Widget_SetValue_Value:_value,_WidgetId:_value():
            pass

        '''
            Set the value of the given widget. Updates the UserInterface Extensions status tree. Returns an error if the value is out of range.
        '''
    def xCommand_UserInterface_Extensions_Widget_UnsetValue_WidgetId:_value():
            pass

        '''
            Empties the value of the given widget. Updates the UserInterface Extensions status tree and notifies the user interface that this widget is no longer selected.
        '''
    def xCommand_UserInterface_LedControl_Color_Set_Color:_value():
            pass

        '''
            
        '''
        class Alert:
            pass

            def Clear():
            pass

        '''
            Remove the message which was displayed using the UserInterface Message Alert Display command. This is required when the Duration parameter is not set.
        '''
    def xCommand_UserInterface_Message_Alert_Display_Duration:_value,_Text:_value,_Title:_value():
            pass

        '''
            Display a message on screen. Optionally you can keep the message for a specified duration of time. If Duration is not set, the command must be followed by a UserInterface Message Alert Clear command.
        '''
    def xCommand_UserInterface_Message_Prompt_Clear_FeedbackId:_value():
            pass

        '''
            Remove the window which was displayed using the UserInterface Message Prompt Display command. This is required when the Duration parameter is not set. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_Prompt_Display_Duration:_value,_FeedbackId:_value,_"Option.1":_value,_"Option.2":_value,_"Option.3":_value,_"Option.4":_value,_"Option.5":_value,_Text:_value,_Title:_value():
            pass

        '''
            Display a small window on screen with a title, text and up to five options for response from the user. The message is displayed on screen until the user gives a response, or until the device receives a UserInterface Message Prompt Clear command. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_Prompt_Response_FeedbackId:_value,_OptionId:_value():
            pass

        '''
            Give a response to the UserInterface Message Prompt Display command. This command is executed when the user selects an option in the user interface. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_Rating_Clear_FeedbackId:_value():
            pass

        '''
            Remove the message which was displayed using the UserInterface Message Rating Display command. This is required when the Duration parameter is not set.
        '''
    def xCommand_UserInterface_Message_Rating_Display_Duration:_value,_FeedbackId:_value,_SubmitReceiptText:_value,_SubmitReceiptTitle:_value,_Text:_value,_Title:_value():
            pass

        '''
            Display a small window on screen with a title and text. Rating stars are provided for the user to select. The message is displayed on screen until the user gives a response, or until the device receives a UserInterface Message Rating Clear command. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_Rating_Response_FeedbackId:_value,_Rating:_value():
            pass

        '''
            Give a response to the UserInterface Message Rating Display command. This command is executed when the user selects an option in the user interface. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_TextInput_Clear_FeedbackId:_value():
            pass

        '''
            Remove the text input message which was displayed using the UserInterface Message TextInput Display command. This is required when the Duration parameter is not set. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_TextInput_Display_Duration:_value,_FeedbackId:_value,_InputText:_value,_InputType:_value,_KeyboardState:_value,_Placeholder:_value,_SubmitText:_value,_Text:_value,_Title:_value():
            pass

        '''
            Displays an input dialog box to which a user can respond. This is only supported for devices with a touch-based user interface. The message is displayed on screen until the user gives a response, or until the device receives a UserInterface Message TextInput Clear command. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
    def xCommand_UserInterface_Message_TextInput_Response_FeedbackId:_value,_Text:_value():
            pass

        '''
            Give a response to the UserInterface Message TextInput Display command. This command is executed when the user submits the reply that he has entered in the text input field in the user interface. Use the xFeedback commands to monitor the feedback from the user. Read more about the xFeedback commands in the API introduction section in this guide.
        '''
        class TextLine:
            pass

            def Clear():
            pass

        '''
            Remove the text line which was displayed by the UserInterface Message TextLine Display command. This is required when the Duration parameter is not set.
        '''
    def xCommand_UserInterface_Message_TextLine_Display_Duration:_value,_Text:_value,_X:_value,_Y:_value():
            pass

        '''
            Display a text line on screen. Optionally you can place the text line at a specified location and for a specified duration of time. If Duration is not set, the command must be followed by the UserInterface Message TextLine Clear command.
        '''
    def xCommand_UserInterface_Presentation_ExternalSource_Add_ConnectorId:_value,_Name:_value,_SourceIdentifier:_value,_Type:_value():
            pass

        '''
            Establish and set up an input source that is connected to the device via an external switch.
        '''
        class ExternalSource:
            pass

            def List():
            pass

        '''
            Returns the current list of external input sources.
        '''
    def xCommand_UserInterface_Presentation_ExternalSource_Remove_SourceIdentifier:_value():
            pass

        '''
            Remove the input source (specified by the SourceIdentifier) from the list of external input sources.
        '''
            def RemoveAll():
            pass

        '''
            Remove all input sources from the list of external input sources.
        '''
    def xCommand_UserInterface_Presentation_ExternalSource_Select_SourceIdentifier:_value():
            pass

        '''
            Starts to present the input source (specified by the SourceIdentifier) if it is in Ready state (see the UserInterface Presentation ExternalSource State Set command). The input source will be shown in the user interface sharetray as "Presenting".
        '''
    def xCommand_UserInterface_Presentation_ExternalSource_State_Set_ErrorReason:_value,_SourceIdentifier:_value,_State:_value():
            pass

        '''
            Set or change the state of the input source (specified by the SourceIdentifier).
        '''
        class Override:
            pass

            def Clear():
            pass

        '''
            Clear all translation overrides.
        '''
            def Get():
            pass

        '''
            Returns the translation override information in JSON format. If no translation override is set, it will return an error.
        '''
    def xCommand_UserInterface_Translation_Override_Set_Raw_data_here..._Must_end_with_line_with_single_dot_.():
            pass

        '''
            Set a translation override for text on the user interface. For instance, change the title "Whiteboard" to "whiteboard collection", or whatever you like. This is a multiline command that expects the override set in JSON format. For example: { "version": 1, "translations": [ { "sourceText": "Whiteboard", "translated": "WB", "language": "English" } ] } sourceText: The English version of the text to be replaced. translated: The text to use as the replacement for the language th...
        '''
    class WallpaperBundle:
        pass

        def Clear():
            pass

        '''
            Not applicable in this release.
        '''
        def List():
            pass

        '''
            Not applicable in this release.
        '''
    def xCommand_UserInterface_WallpaperBundle_Set_Name:_value():
            pass

        '''
            Not applicable in this release.
        '''
    def xCommand_UserInterface_WebView_Clear_Target:_value():
            pass

        '''
            Closes the current web view.
        '''
    def xCommand_UserInterface_WebView_Display_Header:_value,_Mode:_value,_Options:_value,_Target:_value,_Title:_value,_Url:_value():
            pass

        '''
            Opens the web view and displays the web page given by the URL.
        '''
class UserManagement:
    def __init__(self) -> str:
        pass

    def xCommand_UserManagement_RemoteSupportUser_Create_ExpiryDays:_value():
            pass

        '''
            Create a remote support user passphrase that Technical Assistance Center (TAC) can use to access the device for troubleshooting.
        '''
    class RemoteSupportUser:
        pass

        def Delete():
            pass

        '''
            Delete the remote support user created with the command xCommand UserManagement RemoteSupportUser Create.
        '''
    def xCommand_UserManagement_RemoteSupportUser_DisablePermanently_Confirm:_value():
            pass

        '''
            Disable the creation of new remote support users. To enable the remote support user again you must factory reset your device.
        '''
        def GetState():
            pass

        '''
            Retrieves the state of the generated remote support user, if one exists.
        '''
    def xCommand_UserManagement_User_Add_Active:_value,_ClientCertificateDN:_value,_Passphrase:_value,_PassphraseChangeRequired:_value,_Role:_value,_ShellLogin:_value,_Username:_value,_YourPassphrase:_value():
            pass

        '''
            Adds a new user to this device.
        '''
    def xCommand_UserManagement_User_Delete_Username:_value,_YourPassphrase:_value():
            pass

        '''
            Deletes a user from this device.
        '''
    def xCommand_UserManagement_User_Get_ClientCertificateDN:_value,_Username:_value():
            pass

        '''
            Shows the details of users on this device.
        '''
    def xCommand_UserManagement_User_List_Limit:_value,_Offset:_value():
            pass

        '''
            Shows the list of users on this device.
        '''
    def xCommand_UserManagement_User_Modify_Active:_value,_AddRole:_value,_ClientCertificateDN:_value,_PassphraseChangeRequired:_value,_RemoveRole:_value,_ShellLogin:_value,_Username:_value,_YourPassphrase:_value():
            pass

        '''
            Modifies the details of a particular user.
        '''
    def xCommand_UserManagement_User_Unblock_Username:_value,_YourPassphrase:_value():
            pass

        '''
            Unblocks a user who is blocked out because of too many failed login attempts.
        '''
    def xCommand_UserManagement_User_Passphrase_Change_NewPassphrase:_value,_OldPassphrase:_value():
            pass

        '''
            Change the passphrase for the user you logged in as. If you are logged in as the administrator, this will change the administrator passphrase.
        '''
    def xCommand_UserManagement_User_Passphrase_Set_NewPassphrase:_value,_Username:_value,_YourPassphrase:_value():
            pass

        '''
            Set a user passphrase for the specified user. You must be logged in as an administrator to set a user passphrase.
        '''
class Video:
    def __init__(self) -> str:
        pass

    def xCommand_Video_ActiveSpeakerPIP_Set_Position:_value():
            pass

        '''
            Sets position for the active speakers PiP (picture in picture).
        '''
    def xCommand_Video_CEC_Input_KeyClick_ConnectorId:_value,_Key:_value,_LogicalAddress:_value,_NamedKey:_value():
            pass

        '''
            Mimics a remote control key click event from the input device.
        '''
    def xCommand_Video_CEC_Output_KeyClick_ConnectorId:_value,_Key:_value,_LogicalAddress:_value,_NamedKey:_value():
            pass

        '''
            Mimics a remote control key click event from this device.
        '''
    def xCommand_Video_CEC_Output_SendActiveSourceRequest_ConnectorId:_value():
            pass

        '''
            A request from the video conferencing device to become the active source of the screen (device) that is connected to the specified output connector.
        '''
    def xCommand_Video_CEC_Output_SendInactiveSourceRequest_ConnectorId:_value():
            pass

        '''
            A request from the video conferencing device to stop being the active source of the screen (device) that is connected to the specified output connector. It is up to the screen to decide how to respond to the request. It can become the active source itself, make another source the active one, or do nothing.
        '''
    def xCommand_Video_Graphics_Clear_Target:_value():
            pass

        '''
            Remove a text string that has been added to the main video stream, the presentation stream, or the local output using the Video Graphics Text Display command. If you don't want to remove the text string from all those places, you can use multiple Target parameters to choose a subset.
        '''
    def xCommand_Video_Graphics_Text_Display_Date:_value,_Duration:_value,_Target:_value,_Text:_value,_Time:_value():
            pass

        '''
            Compose a text string that will be added to the main video stream, the presentation stream, and the local output. If you don't want to add the text string all those places, you can use multiple Target parameters to choose a subset.
        '''
    def xCommand_Video_Input_SetMainVideoSource_ConnectorId:_value,_Layout:_value,_PIPPosition:_value,_PIPSize:_value,_SourceId:_value():
            pass

        '''
            Set which input source is the main video source. You can identify the input source by either the physical connector that it is connected to (ConnectorId) or the logical source identifier (SourceId). You can combine multiple input sources in a single main video stream (the maximum number of different input sources depend on the type of video conferencing device) by adding multiple ConnectorIds or SourceIds in the same command. There cannot be a mix of identifier types in the same command; use eit...
        '''
        class MainVideo:
            pass

            def Mute():
            pass

        '''
            Stop sending video from the device. Selfview is also turned off. This command does not affect the presentation channel.
        '''
            def Unmute():
            pass

        '''
            Start sending video from the device if previously turned off using the Video Input MainVideo Mute command (or, if available, the "Turn off video" button on the user interface). Selfview is also available.
        '''
    def xCommand_Video_Layout_SetLayout_LayoutName:_value():
            pass

        '''
            Select which video layout family to use locally. You must choose a value from the list returned by the Video Layout CurrentLayouts AvailableLayouts[n] LayoutName status.
        '''
    def xCommand_Video_Layout_LayoutFamily_Set_CustomLayoutName:_value,_LayoutFamily:_value,_Target:_value():
            pass

        '''
            Select which video layout family to use locally. This setting applies only when using a device's built-in MultiSite feature (optional) to host a multipoint video conference.
        '''
    def xCommand_Video_Matrix_Assign_Layout:_value,_Mode:_value,_Output:_value,_RemoteMain:_value,_SourceId:_value():
            pass

        '''
            Video Matrix commands are a smart overlay to the xCommand Video Layout commands to make it easy to do simple video compositions.
        '''
    def xCommand_Video_Matrix_Reset_Output:_value():
            pass

        '''
            Reset the content on the output to the default layout xCommand Video Matrix commands are a smart overlay to the xCommand Video Layout commands to make it easy to do simple video compositions.
        '''
    def xCommand_Video_Matrix_Swap_OutputA:_value,_OutputB:_value():
            pass

        '''
            Swap the content defined with xCommand Video Matrix Assign between two outputs. xCommand Video Matrix commands are a smart overlay to the xCommand Video Layout commands to make it easy to do simple video compositions.
        '''
    def xCommand_Video_Matrix_Unassign_Output:_value,_RemoteMain:_value,_SourceId:_value():
            pass

        '''
            Remove a source from an output. Just as with xCommand Video Matrix Assign the layout engine will recompose the remaining sources automatically. xCommand Video Matrix commands are a smart overlay to the xCommand Video Layout commands to make it easy to do simple video compositions.
        '''
    def xCommand_Video_PresentationPIP_Set_Position:_value():
            pass

        '''
            Sets position for the presentation PiP (picture in picture).
        '''
    def xCommand_Video_PresentationView_Set_View:_value():
            pass

        '''
            Set the presentation view mode
        '''
    def xCommand_Video_Selfview_Set_FullscreenMode:_value,_Mode:_value,_OnMonitorRole:_value,_PIPPosition:_value():
            pass

        '''
            Sets self-view on/off and specifies its size and position. If the parameter is not specified, current value is used.
        '''
class VoiceControl:
    def __init__(self) -> str:
        pass

class WebEngine:
    def __init__(self) -> str:
        pass

    def xCommand_WebEngine_DeleteStorage_Type:_value():
            pass

        '''
            Deletes session data for web view types, such as digital signage and web apps.
        '''
class WebRTC:
    def __init__(self) -> str:
        pass

    def xCommand_WebRTC_Join_BookingId:_value,_MeetingNumber:_value,_Title:_value,_Type:_value,_Url:_value():
            pass

        '''
            Join a WebRTC meeting (e.g., Microsoft Teams, Google Meet). WebRTC is only available for devices that are registered to an on-premises service and linked to Webex Edge for Devices, and for devices that are registered to the Webex cloud service.
        '''
    def xCommand_WebRTC_Provider_Current_Diagnostics_Send():
            pass

        '''
            Sends diagnostics from the WebRTC meeting app (e.g., Microsoft Teams) to the meeting provider (e.g., Microsoft). These diagnostics are not available to Cisco. WebRTC is only available for devices that are registered to an on-premises service and linked to Webex Edge for Devices, and for devices that are registered to the Webex cloud service.
        '''
    def xCommand_WebRTC_Provider_GoogleMeet_MeetingNumber_Validate_MeetingNumber:_value():
            pass

        '''
            Validates the meeting number provided for a Google Meet meeting. WebRTC is only available for devices that are registered to an on-premises service and linked to Webex Edge for Devices, and for devices that are registered to the Webex cloud service. Google Meet is not currently available on Webex Desk.
        '''
class Webex:
    def __init__(self) -> str:
        pass

    def xCommand_Webex_Join_DisplayName:_value,_Number:_value,_TrackingData:_value():
            pass

        '''
            Join the Webex Meeting specified by the meeting number. Add optional information, such as the display name or a tag, to identify the call in the call history.
        '''
    class Registration:
        pass

        def Cancel():
            pass

        '''
            Cancel device registration to Cisco Webex. This command only works in the short period after the registration is started with xCommand Webex Registration Start.
        '''
    def xCommand_Webex_Registration_ConvertToCloud_Confirm:_value():
            pass

        '''
            Convert a device to be managed by the Cisco Webex cloud service. This is only available on systems linked with Webex Edge for Devices. All current connections to on-premises services for calling and directory will be replaced with cloud data sources. To convert back to on-premises again, the device must factory reset.
        '''
        def Logout():
            pass

        '''
            Log a user out from a personalized system, typically Hot Desked shared system or personalized Webex Edge device.
        '''
    def xCommand_Webex_Registration_Start_AccountLinkMode:_value,_ActivationCode:_value,_RegistrationType:_value,_SecurityAction:_value():
            pass

        '''
            Start registering a device to Cisco Webex cloud service by entering the activation code that has been created in Control Hub and choosing whether to keep local users and integrations. You get a confirmation that the registration has been successful or failed.
        '''
