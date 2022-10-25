'''
Appearance
Integer 1 - 999999999
Only for Cisco internal use.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Pro 55, Board Pro 75, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Codec Plus, Codec Pro, Room 55, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Single, Room 70 Single G2, Room Kit, Room Kit Mini
Privacy impacting ⚠️ Yes
'''

def Dial():                
    """Dial out from the device. Returns information about the CallId and ConferenceId,
    which are required for some of the other commands."""                
    return "xCommand Dial"

'''
Device
Required Literal Internal, HeadsetUSB, HandsetUSB
Choose whether to use the built-in loudspeakers and microphone (internal), a Bluetooth® headset (Desk Series and Board Pro only), an analog headset (Desk Pro and Desk Limited Edition only), a USB headset, or a USB handset.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

class Audio:

    def Select():                
        """Select which type of audio device to use (built-in loudspeakers and microphone,
        headsets, or handset)."""                
        return "xCommand Audio Select"

'''
MeasurementLength
Integer 1 - 100 Default: 6
The length of the measurement in number of seconds. In a noisy environment a longer measurement duration will give a more reliable and robust result.
'''

'''
Back-end Any
User roles Admin, User
Products Room Series
Privacy impacting No
'''

    class Diagnostics:
    
        def MeasureDelay():                
            """This command measures the audio delay/latency in a device that is connected to
            the video conferencing device. A typical use case it to measure the delay in a
            TV connected to the video conferencing device via the HDMI connector. If the
            delay in a TV is too high, the real-time experience of a video call will be
            substantially degraded. If the delay is more than 50 ms we recommend the user to
            find a TV setting that has shorter delay. Typical TV settings that can reduce
            the delay are: Gaming Mode and..."""                
            return "xCommand Audio Diagnostics MeasureDelay"

'''
Channel
Integer 0 - 13 Default: 0
The channel number, from left to right, of the selected output.
'''

'''
Back-end Any
User roles Admin, User
Products Room Series
Privacy impacting No
'''

        class Advanced:
        
            def Run():                
                """This command sends out a noise signal sequentially on all audio output
                connectors and measures the room impulse response (RIR) between the output and
                the microphones. If a RIR is detected, the detected number of microphones
                (input), the detected number of output connectors, and the detected delay
                between the output and input is reported back. Example: xCommand Audio
                Diagnostics Advanced Run Volume: 50 MeasurementLength: 1 Result returned -> OK
                *r AdvancedRunResult (status=OK): *r AdvancedRunResu..."""                
                return "xCommand Audio Diagnostics Advanced Run"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class AecReverb:
        
            def Reset():                
                """Reset the acoustic echo cancellation. This command is useful when making changes
                in the acoustical treatment of the room. All previous adaptations are cleared
                and a new measurement of the reverberation time is made. This is not allowed
                during a call."""                
                return "xCommand Audio Diagnostics AecReverb Reset"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Run():                
                """The command uses the acoustic echo canceller to give an estimate of the
                reverberation time in the room. This is done transparently, without interruption
                of the normal operation of the endpoint."""                
                return "xCommand Audio Diagnostics AecReverb Run"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Microphones:
    
        def Mute():                
            """Mute all microphones."""                
            return "xCommand Audio Microphones Mute"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def ToggleMute():                
            """Toggle the microphone between muted and unmuted."""                
            return "xCommand Audio Microphones ToggleMute"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Unmute():                
            """Unmute all microphones."""                
            return "xCommand Audio Microphones Unmute"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class MusicMode:
        
            def Start():                
                """Start using MusicMode in the current call. Music mode allows the dynamic range
                of music go through. When Music mode is in use, sound level variations are
                transmitted intact and the noise filtering is kept to a minimum. MusicMode is
                automatically turned off when the call ends."""                
                return "xCommand Audio Microphones MusicMode Start"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Stop():                
                """Stop using MusicMode in the current call."""                
                return "xCommand Audio Microphones MusicMode Stop"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class NoiseRemoval:
        
            def Activate():                
                """Activate noise removal on the device. For this to take effect, you need to
                enable xConfiguration Audio Microphones NoiseRemoval Mode to enable the noise
                removal feature on the device."""                
                return "xCommand Audio Microphones NoiseRemoval Activate"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Deactivate():                
                """Deactivate noise removal on the device."""                
                return "xCommand Audio Microphones NoiseRemoval Deactivate"

'''
ConnectorId
Required Integer 1 - 2
'''

'''
Back-end Any
User roles Admin, Integrator
Products Codec Plus, Room Kit
Privacy impacting No
'''

        class Passthrough:
        
            def Start():                
                """"""                
                return "xCommand Audio Microphones Passthrough Start"

'''
ConnectorId
Integer 1 - 2
'''

'''
Back-end Any
User roles Admin, Integrator
Products Codec Plus, Room Kit
Privacy impacting No
'''

            def Stop():                
                """"""                
                return "xCommand Audio Microphones Passthrough Stop"

'''
Loop
Literal Off, On Default: Off
Determines whether or not to loop the playout of the audio sound. The sound is looped by default. Irrespective of how this parameter is set, some of the sounds (Busy, CallWaiting, Dial, Ringing, and SpecialInfo) will play until the Audio Sound Stop command is issued.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Sound:
    
        def Play():                
            """Play a specified audio sound."""                
            return "xCommand Audio Sound Play"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Stop():                
            """Stop playing audio sound."""                
            return "xCommand Audio Sound Stop"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class SoundsAndAlerts:
    
        class Ringtone:
        
            def List():                
                """List all available ringtones. Use the xConfiguration Audio SoundsAndAlerts
                RingTone setting to choose a ringtone."""                
                return "xCommand Audio SoundsAndAlerts Ringtone List"

'''
Loop
Literal Off, On Default: Off
Repeats the chosen ringtone in a loop. To turn off the audio, use the Audio SoundsAndAlerts Ringtone Stop xCommand.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Play():                
                """Play one of the available ringtones. Use the xCommand Audio SoundsAndAlerts
                Ringtone List command to get a list of the available ringtones."""                
                return "xCommand Audio SoundsAndAlerts Ringtone Play"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Stop():                
                """Stops the chosen ringtone from playing. To start playing the ringtone again, use
                the Audio SoundsAndAlerts Ringtone Play xCommand."""                
                return "xCommand Audio SoundsAndAlerts Ringtone Stop"

'''
Device
Literal Internal, HeadsetUSB, HandsetUSB
Choose whether to decrease the volume on the built-in loudspeakers, a USB headset, or a USB handset.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

    class Volume:
    
        def Decrease():                
            """Decrease the volume on one of the video conferencing device's audio units
            (built-in loudspeakers, headsets, or handset). By default, the volume is
            decreased by 5 steps (each step is 0.5 dB). Use the Steps parameter if you want
            to override the default behavior. You can use the optional Device parameter to
            specify which audio unit to address. The most recently selected unit is chosen
            if you don't specify a unit (see xStatus Audio SelectedDevice). Also refer to
            xCommand Audio Select."""                
            return "xCommand Audio Volume Decrease"

'''
Device
Literal Internal, HeadsetUSB, HandsetUSB
Choose whether to increase the volume on the built-in loudspeakers, a USB headset, or a USB handset.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def Increase():                
            """Increase the volume on one of the video conferencing device's audio units
            (built-in loudspeakers, headsets, or handset). By default, the volume is
            increased by 5 steps (each step is 0.5 dB). Use the Steps parameter if you want
            to override the default behavior. You can use the optional Device parameter to
            specify which audio unit to address. The most recently selected unit is chosen
            if you don't specify a unit (see xStatus Audio SelectedDevice). Also refer to
            xCommand Audio Select."""                
            return "xCommand Audio Volume Increase"

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def Mute():                
            """Mute the volume on the selected audio unit (built-in loudspeakers, headsets, or
            handset). Refer to the xStatus Audio SelectedDevice and xCommand Audio Select
            commands for more information about the selected audio unit."""                
            return "xCommand Audio Volume Mute"

'''
Device
Literal Internal, HeadsetUSB, HandsetUSB
Choose whether to set the volume on the built-in loudspeakers, a USB headset, or a USB handset.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def Set():                
            """Set the volume on one of the video conferencing device's audio units (built-in
            loudspeakers, headsets, or handset) to a specified level. You can use the
            optional Device parameter to specify which audio unit to address. The most
            recently selected unit is chosen if you don't specify a unit (see xStatus Audio
            SelectedDevice). Also refer to xCommand Audio Select."""                
            return "xCommand Audio Volume Set"

'''
Device
Literal Internal, HeadsetUSB, HandsetUSB
Choose whether to set the volume on the built-in loudspeakers, a USB headset, or a USB handset.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def ToggleMute():                
            """Toggle the loudspeaker between muted and unmuted."""                
            return "xCommand Audio Volume ToggleMute"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Unmute():                
            """Set the volume on the device back on after muting."""                
            return "xCommand Audio Volume Unmute"

'''
ConnectorId
Required Integer 1 - 3
The meaning of the connector number depends on the ConnectorType. Refer to the ConnectorType description for details.
'''

'''
Back-end Any
User roles Admin, User
Products Codec Plus, Room 55, Room 55 Dual, Room 70 Dual, Room 70 Single, Room Kit
Privacy impacting ⚠️ Yes
'''

    class VuMeter:
    
        def Start():                
            """Start a VU meter to measure the audio signal level on the specified connector.
            You must specify both the connector's type and number (ConnectorType,
            ConnectorId) to uniquely identify the connector and behavior. The VU meter
            measures the input level for frequencies below 20 kHz. You can monitor the
            measured signal levels on the device's local web interface (Settings > Audio and
            Video), or you can use the xFeedback and xEvents commands."""                
            return "xCommand Audio VuMeter Start"

'''
ConnectorId
Required Integer 1 - 3
Specify the connector number. In general, the connector number is a unique ID that identifies the microphone input. The connector numbers available depend on the device. Refer to the Audio VuMeter Start command for a detailed description.
'''

'''
Back-end Any
User roles Admin, User
Products Codec Plus, Room 55, Room 55 Dual, Room 70 Dual, Room 70 Single, Room Kit
Privacy impacting ⚠️ Yes
'''

        def Stop():                
            """Stop the VU meter on the specified connector. You must specify both the
            connector's type and number (ConnectorType, ConnectorId) to uniquely identify
            the connector."""                
            return "xCommand Audio VuMeter Stop"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def StopAll():                
            """Stop all VU meters."""                
            return "xCommand Audio VuMeter StopAll"

'''
BookingRequestUUID
String 1 - 128
A unique identifier for the booking request. If this parameter is omitted, a booking request identifier will be assigned automatically.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class Bookings:

    def Book():                
        """Book the meeting room for the specified period. If you don’t specify the start
        time and duration, the room will be booked from now on and for 30 minutes. This
        command is only available for devices that support the room scheduling feature,
        refer to the RoomScheduler Enabled setting."""                
        return "xCommand Bookings Book"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Clear():                
        """Clear the current stored list of bookings."""                
        return "xCommand Bookings Clear"

'''
MeetingId
Required String 1 - 128
A unique meeting identifier. It is assigned to the meeting by the calendar service backend. The meeting identifier is returned by the Bookings List command. Note that this is different from the booking request identifier (BookingRequestUUID) that is provided when issuing the Bookings Book command.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Delete():                
        """Remove the meeting that is identified by the MeetingId parameter. Then the room
        becomes available for new bookings. This command is only available for devices
        that support the room scheduling feature, refer to the RoomScheduler Enabled
        setting."""                
        return "xCommand Bookings Delete"

'''
Id
Required String 1 - 128
A unique meeting identifier. It is assigned to the meeting by the calendar service backend. The meeting identifier is returned by the Bookings List command. Note that this is different from the booking request identifier (BookingRequestUUID) that is provided when issuing the Bookings Book command.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Get():                
        """Get the booking information for a specific ID."""                
        return "xCommand Bookings Get"

'''
DayOffset
Integer 0 - 365 Default: 0
Which day to start the search from (today: 0, tomorrow: 1, …).
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def List():                
        """List the stored bookings for the device. The list of booking details is received
        from the management system. All parameters are optional and can be used to limit
        the search result. If no parameters are set, past, present and future bookings
        are all listed. To avoid listing bookings from yesterday and before, use
        DayOffset = 0."""                
        return "xCommand Bookings List"

'''
Id
String 0 - 128
The ID of the notification snooze setting.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def NotificationSnooze():                
        """Sets notifications for the stored bookings in this device to snooze."""                
        return "xCommand Bookings NotificationSnooze"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Put():                
        """This command applies to devices that are either registered to the Webex cloud
        service or registered to an on-premises service and linked to Webex Edge for
        Devices. NOTE: This API has special terms and conditions, please refer to the
        “About the API – Terms and Conditions” section in the API guide. Replace the
        list of stored bookings. This is a multiline command, with details of the stored
        bookings as payload. The meeting information is provided in JSON format. For
        example: { "Bookings": [ { ..."""                
        return "xCommand Bookings Put"

'''
MeetingId
Required String 1 - 128
The unique identifier for the meeting.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Respond():                
        """Accept or decline a meeting invitation. This command applies to devices that are
        either registered to the Webex cloud service or registered to an on-premises
        service and linked to Webex Edge for Devices."""                
        return "xCommand Bookings Respond"

'''
CallId
Integer 0 - 65534 Default: 0
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class Call:

    def Accept():                
        """Accept an incoming call. If no CallId is specified, all incoming calls are
        accepted."""                
        return "xCommand Call Accept"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During the call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def DTMFSend():                
        """Send DTMF tones to the far end."""                
        return "xCommand Call DTMFSend"

'''
CallId
Integer 0 - 65534 Default: 0
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During the call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Disconnect():                
        """Disconnect a call. If no CallId is specified, the currently active call will be
        disconnected."""                
        return "xCommand Call Disconnect"

'''
DisplayName
Required String 0 - 255
The local reference for the forwarded destination.
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Forward():                
        """Specifies what number or URI you want to forward your incoming calls to. The
        display name is a local reference for the forwarded destination. A message,
        together with the local reference, is shown on screen when you have configured
        the device to forward all calls."""                
        return "xCommand Call Forward"

'''
CallId
Integer 0 - 65534 Default: 0
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Hold():                
        """Put a call on hold."""                
        return "xCommand Call Hold"

'''
CallId
Required Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Ignore():                
        """Turns off the ringtone for the incoming call. The call can still be answered."""                
        return "xCommand Call Ignore"

'''
CallId
IntegerArray 0 - 65534
You can have from 1 to 10 CallId parameters in the same command.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Join():                
        """Cisco internal use only."""                
        return "xCommand Call Join"

'''
CallId
Integer 0 - 65534 Default: 0
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Reject():                
        """Reject incoming call. If no call id is specified, all incoming calls are
        rejected."""                
        return "xCommand Call Reject"

'''
CallId
Integer 0 - 65534 Default: 0
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Resume():                
        """Resume a call that have been put on hold."""                
        return "xCommand Call Resume"

'''
CallId
Required Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def UnattendedTransfer():                
        """Transfers an ongoing call to another participant. Fully supported for SIP calls
        only."""                
        return "xCommand Call UnattendedTransfer"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is required to identify the far end device only when in a Multipoint call. The CallId is returned when issuing the xCommand Dial command. You can get the callId during the call, by running xStatus Call from one of the devices participating in the call.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class FarEndControl:
    
        class Source:
        
            def Select():                
                """Select which video input source to use as the main source on the far end device.
                This command can be issued from a device that is participating in a call and can
                be used to select the source for another device within the same call. For on-
                premises and CMS, this command selects the source for the active speaker. For
                cloud, this command selects the source of the specified participant. An
                additional constraint is that you cannot control the source of a cloud-based
                personal mode device. This is for ..."""                
                return "xCommand Call FarEndControl Source Select"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is a unique number used to address an active call. You can get the callId during the call, by running xStatus Call from one of the devices participating in the call.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class Camera:
        
            def Move():                
                """Move the far end camera (the remote camera). This command can be issued from a
                device that is participating in a call and can be used to control the camera of
                another device within the same call. Speakertrack must be disabled on the far
                end camera. Once the Move command is issued, the far end camera will continue to
                move in the specified direction until the stop command (ref: xCommand
                FarEndControl Camera Stop) is issued. For on-premises and CMS, this command
                accesses the camera of the active sp..."""                
                return "xCommand Call FarEndControl Camera Move"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is a unique number used to address an active call. You can get the callId during the call, by running xStatus Call from one of the devices participating in the call.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Stop():                
                """Stop the far end camera after the xCommand FarEndControl Camera Move has been
                issued. This command can be issued from a device that is participating in a call
                and can be used to control the camera of another device within the same call.
                Speakertrack must be disabled on the far end camera. For on-premises and CMS,
                this command accesses the camera of the active speaker. For cloud, this command
                accesses the camera of the specified participant. An additional constraint is
                that you cannot control the..."""                
                return "xCommand Call FarEndControl Camera Stop"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is required to identify the far end device only when in a Multipoint call. The CallId is returned when issuing the xCommand Dial command. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class RoomPreset:
        
            def Activate():                
                """While in a call, this command is used to activate a preset on the far end
                device. The preset covers the far end device's camera positions and input video
                switcher settings. The preset must be stored on the far end device beforehand,
                either by using the xCommand Preset Store command locally on the far end device,
                or by using the xCommand FarEndControl Preset Store command from a remote
                device. Note: The far end device's xConfiguration Conference FarEndControl Mode
                setting must be switched On for ..."""                
                return "xCommand Call FarEndControl RoomPreset Activate"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is required to identify the far end device only when in a Multipoint call. The CallId is returned when issuing the xCommand Dial command. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Store():                
                """While in a call, this command is used to store a preset on the far end device.
                The preset covers the far end device's camera positions and input video switcher
                settings. Note: The far end device's xConfiguration Conference FarEndControl
                Mode setting must be switched On for the FarEndControl commands to work."""                
                return "xCommand Call FarEndControl RoomPreset Store"

'''
CallId
Integer 0 - 65534 Default: -1
The CallId is required to identify the far end device only when in a Multipoint call. The CallId is returned when issuing the xCommand Dial command. You can get the callId during the call, by running xStatus Call from one of the devices participating in the call.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the xCommand Dial command is run. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class FarEndMessage:
    
        def Send():                
            """Send data between two codecs in a point-to-point call, for use with control
            systems or macros. Works with SIP calls only. Requires that the Conference
            FarEndMessage Mode is set to On."""                
            return "xCommand Call FarEndMessage Send"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class CallHistory:

    def AcknowledgeAllMissedCalls():                
        """Turns off the missed calls indicator on the touch controller for all missed
        calls."""                
        return "xCommand CallHistory AcknowledgeAllMissedCalls"

'''
AcknowledgeConsecutiveDuplicates
Literal False, True Default: False
You can include or exclude all surrounding calls with duplicate information.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def AcknowledgeMissedCall():                
        """Turns off the missed calls indicator on the touch controller for the specified
        call."""                
        return "xCommand CallHistory AcknowledgeMissedCall"

'''
Filter
Literal All, Missed, Placed, Received Default: All
You can filter which calls to delete.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def DeleteAll():                
        """Deletes all information on previous calls."""                
        return "xCommand CallHistory DeleteAll"

'''
CallHistoryId
Required Integer 1 - 2147483647
CallHistoryId for the call in question. Run xCommand CallHistory Get to get the id number.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def DeleteEntry():                
        """Deletes all information on the specified call."""                
        return "xCommand CallHistory DeleteEntry"

'''
CallHistoryId
Integer 1 - 2147483647
CallHistoryId for the call in question.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Get():                
        """Retrieve all information on previous calls made on the device."""                
        return "xCommand CallHistory Get"

'''
DetailLevel
Literal Basic, Full Default: Basic
Sets the level of detail for the information on these calls.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Recents():                
        """Retrieve aggregated information on previous calls made on the device."""                
        return "xCommand CallHistory Recents"

'''
CameraId
Required Integer 1 - 1
The ID of the camera preset you want to reset.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board 55, Board 55S, Board 70, Board 70S, Board 85S, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

class Camera:

    def PositionSet():                
        """Set the camera position. If the combination of the pan, tilt, zoom, and roll
        values is not possible, the camera automatically adjusts the values to a valid
        combination."""                
        return "xCommand Camera PositionSet"

'''
CameraId
Required Integer 1 - 1
Select the camera.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board 55, Board 55S, Board 70, Board 70S, Board 85S, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

    def Ramp():                
        """Move the camera in a specified direction. The camera moves at specified speed
        until a stop command is issued. In a daisy chain, you need to know the CameraId
        for the camera you want to address. Be aware that pan and tilt can be operated
        simultaneously, but no other combinations. In the latter case only the first
        operation specified is executed. For example, if you try to run both zoom and
        pan at the same time, only zoom is executed. NOTE: You must run a stop command
        to stop the camera, see the e..."""                
        return "xCommand Camera Ramp"

'''
PresetId
Required Integer 1 - 35
The ID of the camera preset you want to activate.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Preset:
    
        def Activate():                
            """Activate one of the stored camera presets. This command has no effect on speaker
            tracking. If speaker tracking is on, it will continue from the preset position.
            Note that the xCommand Camera Preset commands applies to an individual camera."""                
            return "xCommand Camera Preset Activate"

'''
CameraId
Integer 1 - 1
The ID of the camera preset you want to activate. If CameraId is not specified, all cameras will be set in their respective default position, if one is defined.
'''

'''
Back-end Any
User roles Admin, User
Products Board 55, Board 55S, Board 70, Board 70S, Board 85S, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def ActivateDefaultPosition():                
            """Sets the cameras to their default position, if one is defined. The default
            position is defined by xCommand Camera Preset Store or by xCommand Camera Preset
            Edit. Only one default position can be defined per camera. This command has no
            effect on speaker tracking. If speaker tracking is on, it will continue from the
            preset position."""                
            return "xCommand Camera Preset ActivateDefaultPosition"

'''
DefaultPosition
Literal False, True
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Edit():                
            """Edit a stored camera preset. You can change the name of the camera preset and
            its position in the list that is returned by the xCommand Camera Preset List
            command. You can also change whether or not this preset is the default position
            for the associated camera. Note that the xCommand Camera Preset commands applies
            to an individual camera."""                
            return "xCommand Camera Preset Edit"

'''
CameraId
Integer 1 - 1
Only list presets for the specified camera.
'''

'''
Back-end Any
User roles Admin, User
Products Board 55, Board 55S, Board 70, Board 70S, Board 85S, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def List():                
            """List information about available camera presets. Note that the xCommand Camera
            Preset commands applies to an individual camera."""                
            return "xCommand Camera Preset List"

'''
PresetId
Required Integer 1 - 35
The ID of the camera preset you want to remove.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Remove():                
            """Remove a camera preset. Note that the xCommand Camera Preset commands applies to
            an individual camera."""                
            return "xCommand Camera Preset Remove"

'''
PresetId
Required Integer 1 - 35
The ID of the camera preset you wish to see.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Show():                
            """Shows the preset details for the requested PresetId."""                
            return "xCommand Camera Preset Show"

'''
CameraId
Required Integer 1 - 1
Select the camera for which to store the preset position.
'''

'''
Back-end Any
User roles Admin, User
Products Board 55, Board 55S, Board 70, Board 70S, Board 85S, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def Store():                
            """Store the current position (pan and tilt), zoom and focus of the chosen camera.
            The camera is identified by the CameraId parameter. Note that the xCommand
            Camera Preset commands applies to an individual camera. The xCommand Camera
            Preset commands are useful when you want to handle multiple camera positions
            individually per camera, rather than working with complete sets of camera
            positions. The individual camera presets are not available for far end control."""                
            return "xCommand Camera Preset Store"

'''
Back-end Any
User roles Admin, User
Products Room 55, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Panorama
Privacy impacting No
'''

class Cameras:

    class SpeakerTrack:
    
        def Activate():                
            """Activate SpeakerTrack mode. Requires that xConfiguration Cameras SpeakerTrack
            Mode is set to Auto (default)."""                
            return "xCommand Cameras SpeakerTrack Activate"

'''
Back-end Any
User roles Admin, User
Products Room 55, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Panorama
Privacy impacting No
'''

        def Deactivate():                
            """Deactivate SpeakerTrack mode."""                
            return "xCommand Cameras SpeakerTrack Deactivate"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class BackgroundMode:
        
            def Activate():                
                """"""                
                return "xCommand Cameras SpeakerTrack BackgroundMode Activate"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Deactivate():                
                """"""                
                return "xCommand Cameras SpeakerTrack BackgroundMode Deactivate"

'''
Tracking
Literal On, Off Default: On
The Tracking parameter is not applicable for this product.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Room 55, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Panorama
Privacy impacting No
'''

        class Diagnostics:
        
            def Start():                
                """Starts diagnostics on the camera's speaker tracking."""                
                return "xCommand Cameras SpeakerTrack Diagnostics Start"

'''
Back-end Any
User roles Admin, Integrator, User
Products Room Series
Privacy impacting No
'''

            def Stop():                
                """Stops diagnostics on the camera's tracking."""                
                return "xCommand Cameras SpeakerTrack Diagnostics Stop"

'''
Back-end Any
User roles Admin, Integrator
Products Room Series
Privacy impacting No
'''

        class ViewLimits:
        
            def Activate():                
                """Start using the limited maximum camera view for speaker tracking (see the
                Cameras SpeakerTrack ViewLimits StorePosition command). The full camera range is
                always available for manual camera control."""                
                return "xCommand Cameras SpeakerTrack ViewLimits Activate"

'''
Back-end Any
User roles Admin, Integrator
Products Room Series
Privacy impacting No
'''

            def Deactivate():                
                """Stop using the limited maximum camera view for speaker tracking (see the Cameras
                SpeakerTrack ViewLimits StorePosition command). The fully zoomed-out camera view
                will be used instead."""                
                return "xCommand Cameras SpeakerTrack ViewLimits Deactivate"

'''
Back-end Any
User roles Admin, Integrator
Products Room Series
Privacy impacting No
'''

            def StorePosition():                
                """Store the current camera view as the maximum view (room overview) for speaker
                tracking. This way you can limit the default maximum view to exclude parts of
                the room. If you don't set a limit, the maximum view for speaker tracking is the
                fully zoomed-out camera view."""                
                return "xCommand Cameras SpeakerTrack ViewLimits StorePosition"

'''
CameraId
Required Integer 1 - 1
The ID of the camera that is being positioned.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit
Privacy impacting No
'''

        class Whiteboard:
        
            def ActivatePosition():                
                """Moves the specified camera to the position stored with xCommand Cameras
                SpeakerTrack Whiteboard StorePosition."""                
                return "xCommand Cameras SpeakerTrack Whiteboard ActivatePosition"

'''
Distance
Required Integer 0 - 65534
Set distance to whiteboard in centimeters. Use an accurate measurement for the feature to work seamlessly.
'''

'''
Back-end Any
User roles Admin, User
Products Codec Plus, Codec Pro, Room 55, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Panorama
Privacy impacting No
'''

            def SetDistance():                
                """Set the cameras distance to the whiteboard. This information is needed by the
                camera to frame the whiteboard automatically."""                
                return "xCommand Cameras SpeakerTrack Whiteboard SetDistance"

'''
CameraId
Required Integer 1 - 1
The ID of the camera that is being positioned.
'''

'''
Back-end Any
User roles Admin, User
Products Room 55, Room Kit
Privacy impacting No
'''

            def StorePosition():                
                """Store the position of the specified camera as the Snap to Whiteboard position.
                Frame the image so that there is room around the whiteboard for the speaker. To
                use the Snap to Whiteboard feature it must be enabled with xConfiguration
                Cameras SpeakerTrack Whiteboard Mode and tracking must be enabled with
                xConfiguration Cameras SpeakerTrack Mode."""                
                return "xCommand Cameras SpeakerTrack Whiteboard StorePosition"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class Conference:

    def AdmitAll():                
        """Lets into the call or meeting all participants who are waiting in the virtual
        lobby. Available for Hosts and Cohosts of Webex meetings. The device must either
        be registered to the Webex cloud service or linked to Webex Edge for Devices.
        Participants waiting to be admitted have the status "waiting" in the result from
        the Conference ParticipantList Search command (*r ParticipantListSearchResult
        Participant [n] Status = "waiting")."""                
        return "xCommand Conference AdmitAll"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def EndMeeting():                
        """Ends meeting for all participants. The command is available for Hosts and
        Cohosts of Webex meetings. The device must either be registered to the Webex
        cloud service or linked to Webex Edge for Devices."""                
        return "xCommand Conference EndMeeting"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def HardMute():                
        """Mutes the participants in the call or meeting and prevents them from unmuting
        themselves. The command is available for Hosts and Cohosts of Webex meetings.
        The device must either be registered to the Webex cloud service or linked to
        Webex Edge for Devices."""                
        return "xCommand Conference HardMute"

'''
CallId
Required Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Lock():                
        """Locks Webex meetings by preventing uninvited participants from joining. The
        command is available for Hosts and Cohosts of Webex meetings. The device must
        either be registered to the Webex cloud service or linked to Webex Edge for
        Devices."""                
        return "xCommand Conference Lock"

'''
CallId
Integer 0 - 65534
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def LowerAllHands():                
        """Lower the hands of all conference participants."""                
        return "xCommand Conference LowerAllHands"

'''
AudioMute
Required Literal On, Off
Off: This will do a server-side unmute, but NO local mute state change. Participants can mute/unmute themselves locally, as long as the xCommand Conference HardMute HardMute:On has not been issued. On: All participants, except the speaker and the participant who is currently sharing are being muted from the server side. The participants are not prevented from unmuting themselves locally, as long as the xCommand Conference HardMute HardMute:On has not been issued.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def MuteAll():                
        """Mutes all participants, except the speaker and the participant who is currently
        sharing. The command is available for Hosts and Cohosts of Webex meetings. The
        device must either be registered to the Webex cloud service or linked to Webex
        Edge for Devices."""                
        return "xCommand Conference MuteAll"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def MuteOnEntry():                
        """Decides whether all participants are muted or not when they join the meeting.
        They can unmute and mute themselves later. The command is available for Hosts
        and Cohosts of Webex meetings. The device must either be registered to the Webex
        cloud service or linked to Webex Edge for Devices."""                
        return "xCommand Conference MuteOnEntry"

'''
CallId
Integer 0 - 65534
Unique identifier of the call. During a call, you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def TransferHostAndLeave():                
        """Lets you leave a meeting you are hosting, but allows the other particpants to
        continue the meeting. A new host is assigned automatically"""                
        return "xCommand Conference TransferHostAndLeave"

'''
CallId
Integer 0 - 65534 Default: 0
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Call:
    
        def AuthenticationResponse():                
            """This command is only available for Cisco Webex registered devices. The command
            gives a response to an authentication request based on the Conference Call[n]
            AuthenticationRequest status."""                
            return "xCommand Conference Call AuthenticationResponse"

'''
Timeout
Integer 1 - 20160
Set the number of minutes before Do Not Disturb is switched off. If not set, Do Not Disturb times out after 1440 minutes (24 hours).
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class DoNotDisturb:
    
        def Activate():                
            """This command switches on the Do Not Disturb mode, and the Timeout parameter
            allows you to control when it is switched off again. When Do Not Disturb is
            switched on, all incoming calls are rejected and registered as missed calls. The
            calling side receives a busy signal."""                
            return "xCommand Conference DoNotDisturb Activate"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Deactivate():                
            """Switch off the Do Not Disturb mode. When Do Not Disturb is switched off incoming
            calls come through as normal."""                
            return "xCommand Conference DoNotDisturb Deactivate"

'''
CallId
Integer 0 - 65534
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Hand:
    
        def Lower():                
            """Lower your hand. Use the raise hand feature to let the host know that you have a
            question or a comment. Raise Hand is available in meetings with more than two
            participants. It's not available in meetings started from a Webex space."""                
            return "xCommand Conference Hand Lower"

'''
CallId
Integer 0 - 65534
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Raise():                
            """Raise your hand. Use the raise hand feature to let the host know that you have a
            question or a comment. Raise Hand is available in meetings with more than two
            participants. It's not available in meetings started from a Webex space."""                
            return "xCommand Conference Hand Raise"

'''
CallId
Integer 0 - 65534
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class MeetingAssistant:
    
        def Start():                
            """Not applicable in this version."""                
            return "xCommand Conference MeetingAssistant Start"

'''
CallId
Integer 0 - 65534
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Stop():                
            """Not applicable in this version."""                
            return "xCommand Conference MeetingAssistant Stop"

'''
CallId
Required Integer 0 - 65534
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Participant:
    
        def Admit():                
            """Admits or lets in a participant that is waiting to be admitted into the call or
            meeting. This command is only available Cisco Webex registered devices. A
            participant is waiting to be admitted if he has status "waiting" in the result
            from the Conference ParticipantList Search command (*r
            ParticipantListSearchResult Participant [n] Status = "waiting")."""                
            return "xCommand Conference Participant Admit"

'''
CallId
Required Integer 0 - 65534
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Disconnect():                
            """Disconnects the participant from a call or meeting. It is only possible to
            disconnect a participant if the Conference Call[n] Capabilities
            ParticipantDisconnect status for the meeting shows Available."""                
            return "xCommand Conference Participant Disconnect"

'''
CallId
Required Integer 0 - 65534
Unique identifier of the call. During a call you can run the xStatus Call command to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def LowerHand():                
            """Lower the hand of a participant in a conference."""                
            return "xCommand Conference Participant LowerHand"

'''
AudioMute
Required Literal On, Off
Indicate the desired mute state of the participant.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Mute():                
            """Mutes the participant in the call or meeting. It is only possible to mute a
            participant if the Conference Call[n] Capabilities ParticipantMute status shows
            Available."""                
            return "xCommand Conference Participant Mute"

'''
CallId
Integer 0 - 65534 Default: 0
Unique identifier of the call. During a call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class ParticipantList:
    
        def Search():                
            """Returns details about the participants in the call. The results can be filtered
            by specifying additional parameters."""                
            return "xCommand Conference ParticipantList Search"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Reaction:
    
        def Disable():                
            """Prevents participants from reacting with emojis during a Webex meeting. This
            command is available for Hosts and Cohosts of Webex meetings. The device must
            either be registered to the Webex cloud service or linked to Webex Edge for
            Devices."""                
            return "xCommand Conference Reaction Disable"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Enable():                
            """Allows participants to react with emojis during a Webex meeting. This command is
            available for Hosts and Cohosts of Webex meetings. The device must either be
            registered to the Webex cloud service or linked to Webex Edge for Devices."""                
            return "xCommand Conference Reaction Enable"

'''
CallId
Integer 0 - 65534
The CallId is a unique number used to address an active call. The CallId is returned when the Dial or Webex Join commands are run. During the call you can run xStatus Call to see the CallId.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Send():                
            """Sends a reaction (emoji) during a Webex meeting. The device must either be
            registered to the Webex cloud service or linked to Webex Edge for Devices."""                
            return "xCommand Conference Reaction Send"

'''
ReactionTone
Required Integer 0 - 65534
1 is no skin tone, 2 is the lightest skin tone, and 6 the darkest skin tone option.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Tone():                
            """Selects the skin tone to be used for the emojis sent hereafter. Skin tones are
            available for reactions that use hand gestures, such as thumbs up and clapping
            hands. For personal mode devices the skin tone will persist between calls; for
            shared mode devices it will be reset when a call ends. The device must either be
            registered to the Webex cloud service or linked to Webex Edge for Devices."""                
            return "xCommand Conference Reaction Tone"

'''
CallId
Integer 0 - 65534
Identify CallId for the remote participant.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Recording:
    
        def Pause():                
            """Define if the recording of a meeting shall be paused. When you are recording a
            meeting, you can use this setting if you want to pause the recording. You can
            resume the recording by using the command Conference Recording Resume."""                
            return "xCommand Conference Recording Pause"

'''
CallId
Integer 0 - 65534
Identify CallId for the remote participant.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Resume():                
            """Define if the recording of a meeting shall be resumed. When you are recording a
            meeting, you can use this setting if you want to resume a recording that has
            previously been paused."""                
            return "xCommand Conference Recording Resume"

'''
CallId
Integer 0 - 65534
Identify CallId for the remote participant.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Start():                
            """Define if the meeting shall be recorded. Once you are in a meeting, you can use
            this setting if you want to start recording. Note that the recording commands
            are only available if your infrastructure (Cisco Meeting Server) supports
            recording."""                
            return "xCommand Conference Recording Start"

'''
CallId
Integer 0 - 65534
Identify CallId for the remote participant.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Stop():                
            """Define if the recording of a meeting shall be stoppped. When you are recording a
            meeting, you can use this setting to stop recording."""                
            return "xCommand Conference Recording Stop"

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class SpeakerLock:
    
        def Release():                
            """Releases locked speaker set by xCommand Conference SpeakerLock Set. Default
            voice switching is switched back on."""                
            return "xCommand Conference SpeakerLock Release"

'''
CallId
Integer 0 - 65534 Default: 0
Identify CallId for the remote participant. Only relevant if Target is set to "remote".
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Set():                
            """For manually locking one of the speakers to the prominent speaker position. This
            overrides the default voice switching."""                
            return "xCommand Conference SpeakerLock Set"

'''
ResultSet
Literal Alerts, All, None Default: Alerts
You can filter the diagnostics results to alerts, all or none. If not set, the result will show all results.
'''

'''
Back-end Any
User roles Admin, TouchUser
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Diagnostics:

    def Run():                
        """This command runs self-diagnostics commands on the device."""                
        return "xCommand Diagnostics Run"

'''
AllowInsecureHTTPS
Literal False, True Default: False
If set to True the device skips the certificate validation process, and sends data to the server anyway. If set to False, the server certificate is checked, and data is not sent to the server if the certificate validation fails.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class HttpClient:

    def Delete():                
        """Sends an HTTP(S) Delete request to the server that is specified in the Url
        parameter. You can use the AllowInsecureHTTPS parameter to specify whether or
        not to validate the server's certificate before sending data over HTTPS. This
        parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS
        is set to On. The command returns the HTTP status code along with the data
        returned from the server (HTTP headers and body)."""                
        return "xCommand HttpClient Delete"

'''
AllowInsecureHTTPS
Literal False, True Default: False
If set to True the device skips the certificate validation process, and sends data to the server anyway. If set to False, the server certificate is checked, and data is not sent to the server if the certificate validation fails.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Get():                
        """Sends an HTTP(S) Get request to the server that is specified in the Url
        parameter. You can use the AllowInsecureHTTPS parameter to specify whether or
        not to validate the server's certificate before sending data over HTTPS. This
        parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS
        is set to On. The command returns the HTTP status code along with the data
        returned from the server (HTTP headers and body)."""                
        return "xCommand HttpClient Get"

'''
AllowInsecureHTTPS
Literal False, True Default: False
If set to True the device skips the certificate validation process, and sends data to the server anyway. If set to False, the server certificate is checked, and data is not sent to the server if the certificate validation fails.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Patch():                
        """Sends an HTTP(S) Patch request to the server that is specified in the Url
        parameter. This is a multiline command, so the payload (data) follows after the
        parameters. You can use the AllowInsecureHTTPS parameter to specify whether or
        not to validate the server's certificate before sending data over HTTPS. This
        parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS
        is set to On. The command returns the HTTP status code along with the data
        returned from the server (HTTP hea..."""                
        return "xCommand HttpClient Patch"

'''
AllowInsecureHTTPS
Literal False, True Default: False
If set to True the device skips the certificate validation process, and sends data to the server anyway. If set to False, the server certificate is checked, and data is not sent to the server if the certificate validation fails.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Post():                
        """Sends an HTTP(S) Post request to the server that is specified in the Url
        parameter. You can use the AllowInsecureHTTPS parameter to specify whether or
        not to validate the server's certificate before sending data over HTTPS. This
        parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS
        is set to On. This is a multiline command, so the payload (data) follows after
        the parameters."""                
        return "xCommand HttpClient Post"

'''
AllowInsecureHTTPS
Literal False, True Default: False
If set to True the device skips the certificate validation process, and sends data to the server anyway. If set to False, the server certificate is checked, and data is not sent to the server if the certificate validation fails.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Put():                
        """Sends an HTTP(S) Put request to the server that is specified in the Url
        parameter. You can use the AllowInsecureHTTPS parameter to specify whether or
        not to validate the server's certificate before sending data over HTTPS. This
        parameter has no effect unless the xConfiguration HttpClient AllowInsecureHTTPS
        is set to On. This is a multiline command, so the payload (data) follows after
        the parameters."""                
        return "xCommand HttpClient Put"

'''
Expression
Required String 2 - 200
Regular expression that matches a host name or IP address of an HTTP(S) server.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Allow:
    
        class Hostname:
        
            def Add():                
                """Adds an HTTP(S) server to the list of allowed servers (hosts). The HttpClient
                Allow Hostname commands let you set up and maintain a list of up to ten allowed
                hosts. As long as the list is not empty, you can send HTTP(S) requests only to
                the servers in the list. The check against the list is performed both when using
                insecure (HTTP) and secure (HTTPS) transfer of data."""                
                return "xCommand HttpClient Allow Hostname Add"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Clear():                
                """Removes all HTTP(S) servers from the list of allowed servers (hosts), leaving
                you with an empty list."""                
                return "xCommand HttpClient Allow Hostname Clear"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def List():                
                """Returns the list of allowed HTTP(S) servers (hosts). The HttpClient Allow
                Hostname commands let you set up and maintain a list of up to ten allowed hosts.
                As long as the list is not empty, you can send HTTP(S) requests only to the
                servers in the list. The check against the list is performed both when using
                insecure (HTTP) and secure (HTTPS) transfer of data."""                
                return "xCommand HttpClient Allow Hostname List"

'''
Id
Required Integer 0 - 9
The identifier of the HTTP(S) server you want to remove from the list.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Remove():                
                """Removes an HTTP(S) server from the list of allowed servers (hosts). Use the
                HttpClient Allow Hostname List command to find the indentifier of each entry in
                the list."""                
                return "xCommand HttpClient Allow Hostname Remove"

'''
FeedbackSlot
Required Integer 1 - 4
Deregister the feedback slot that was registered using the xCommand HttpFeedback Register command.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class HttpFeedback:

    def Deregister():                
        """Deregister the HTTP feedback over HTTP(S)."""                
        return "xCommand HttpFeedback Deregister"

'''
FeedbackSlot
Required Integer 1 - 4
Specifies the feedback slot that is enabled.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Enable():                
        """Re-enables a previously registered feedback slot after it has failed and become
        deactivated."""                
        return "xCommand HttpFeedback Enable"

'''
Expression
StringArray 1 - 255
The XPath expression specifies which parts of the Status, Configuration or Event XML documents are monitored. You can have from 0 to 15 XPath expressions in the same command.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    def Register():                
        """Register the device to an HTTP(S) server to return XML feedback over HTTP(S) to
        specific URLs."""                
        return "xCommand HttpFeedback Register"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Logging:

    def SendLogs():                
        """Send logs to the Cisco Webex cloud. These logs can help diagnose and fix issues
        with the device. The command returns a log ID, which an administrator or TAC
        engineer can use to identify and download the logs. For the command to work, the
        device must either be registered to the Webex cloud service or registered to an
        on-premises service and linked to Webex Edge for Devices. Additionally, for
        devices linked to Webex Edge for Devices, the xConfiguration Logging CloudUpload
        Mode must be set to On."""                
        return "xCommand Logging SendLogs"

'''
Duration
Integer 1 - 600
Specify the length of time to perform the extended logging (in seconds).
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class ExtendedLogging:
    
        def Start():                
            """Start running continuous extended logging for the specified duration."""                
            return "xCommand Logging ExtendedLogging Start"

'''
RemovePacketDump
Literal False, True Default: False
Delete or keep the packet dump log file. True: Automatically delete the packet dump log file. False: Do not delete the packet dump log file.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Stop():                
            """Stop running the extended logging process."""                
            return "xCommand Logging ExtendedLogging Stop"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class Macros:

    class Log:
    
        def Clear():                
            """Clears the Macros Logs."""                
            return "xCommand Macros Log Clear"

'''
Offset
Integer 0 - 65534 Default: 0
Shows lines with the same or higher Offset than the one provided.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Get():                
            """Shows the logs for all running macros and for the runtime itself."""                
            return "xCommand Macros Log Get"

'''
Name
Required String 0 - 255
Specifies the name of the macro to activate.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Macro:
    
        def Activate():                
            """Activates a macro created on this device."""                
            return "xCommand Macros Macro Activate"

'''
Name
Required String 0 - 255
The name of the macro to deactivate.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Deactivate():                
            """Deactivates a macro currently running on this device."""                
            return "xCommand Macros Macro Deactivate"

'''
Content
Literal False, True Default: False
Shows the content for the specified Macro or not.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Get():                
            """ShowsTruethe details of a macro created on this device."""                
            return "xCommand Macros Macro Get"

'''
Name
Required String 0 - 255
The name of the macro that is removed.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Remove():                
            """Removes a macro created on this device."""                
            return "xCommand Macros Macro Remove"

'''
Name
Required String 0 - 255
The name of the macro that is removed.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

'''
Name
Required String 0 - 255
The name of the macro that is renamed.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Rename():                
            """Renames a macro created on this device."""                
            return "xCommand Macros Macro Rename"

'''
Name
Required String 0 - 255
The name of the macro that is saved.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Save():                
            """Saves the details of a macro. This is a multiline command."""                
            return "xCommand Macros Macro Save"

'''
Name
Required String 0 - 255
The name of the macro that is set.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class Roles:
        
            def Set():                
                """Sets the role for a macro."""                
                return "xCommand Macros Macro Roles Set"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Runtime:
    
        def Restart():                
            """Restarts all of the macros set up on this device."""                
            return "xCommand Macros Runtime Restart"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Start():                
            """Starts all of the macros set up on this device."""                
            return "xCommand Macros Runtime Start"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Status():                
            """Shows the current status of the macros runtime on this device."""                
            return "xCommand Macros Runtime Status"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Stop():                
            """Stops all of the macros set up on this device."""                
            return "xCommand Macros Runtime Stop"

'''
Text
Required String 0 - 1024
The text that the message contains.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Message:

    def Send():                
        """Triggers a Message Send event which sends text to any listening clients."""                
        return "xCommand Message Send"

'''
AuthenticationPassword
Required String 8 - 255
The authentication password for this USM user. It is used when authenticating the network management system. The authentication password is stored as a localized hashed value on the device.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Network:

    class SNMP:
    
        class USM:
        
            class User:
            
                def Add():                
                    """Creates a user (username and passwords) that a network management system can use
                    to communicate with the video conferencing device using SNMP v3, User-based
                    Security Model (USM). All USM users have equal access rights (read, read-write,
                    or none), refer to the NetworkServices SNMP Mode setting. Authentication and
                    privacy are always on. That is, the device supports only the authPriv security
                    level and the privacy protocol is always AES (Advanced Encryption Standard).
                    This command has no effect on ..."""                
                    return "xCommand Network SNMP USM User Add"

'''
Name
Required String 0 - 32
The name of the user that you want to delete.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

                def Delete():                
                    """Deletes a USM user from the device."""                
                    return "xCommand Network SNMP USM User Delete"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

                def List():                
                    """Returns the list of all USM users that are stored on the device."""                
                    return "xCommand Network SNMP USM User List"

'''
AllowMissingCA
Literal False, True
The policy for allowing a Wi-Fi connection with missing Certificate Authentication (CA). False: Not allowed. True: Allowed
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Wifi:
    
        def Configure():                
            """Configures the device to be able to connect to a specific Wi-Fi network. This is
            only available if Wi-Fi is enabled on the device. You must unplug the Ethernet
            cable before you can connect to Wi-Fi. Both WPA2-only and mixed mode access
            points with WPA2 are supported."""                
            return "xCommand Network Wifi Configure"

'''
SSID
Required String 0 - 255
The SSID for the Wi-Fi connection.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Deletes the specified Wi-Fi network connection from the device. This command is
            only available if Wi-Fi services are turned on and ethernet is disconnected."""                
            return "xCommand Network Wifi Delete"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def List():                
            """Lists the details of the current Wi-Fi connection. This command is only
            available if Wi-Fi services are turned on and ethernet is disconnected."""                
            return "xCommand Network Wifi List"

'''
Duration
Integer 1 - 30 Default: 10
The duration of the Wi-Fi scan, in seconds.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class Scan:
        
            def Start():                
                """Scans for available Wi-Fi networks."""                
                return "xCommand Network Wifi Scan Start"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Stop():                
                """Stops an ongoing Wi-Fi scan."""                
                return "xCommand Network Wifi Scan Stop"

'''
HardwareInfo
String 0 - 100
The device's hardware number.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Peripherals:

    def Connect():                
        """Register peripherals that are connected to the device, such as control systems
        and touch panels. The registered peripherals are displayed on the web interface
        under Configuration > Peripherals. This command should be used when the
        peripheral connects to the codec for the first time or when the software version
        on the peripheral has changed. The list of connected devices is available in the
        Peripherals ConnectedDevice [n] Status status."""                
        return "xCommand Peripherals Connect"

'''
ID
Required String 1 - 100
A unique ID for the device you are connecting to, typically a MAC address.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def HeartBeat():                
        """When a peripheral is registered as a connected device, you can set it to send a
        heartbeat to the codec to let the codec know that it is still connected. This
        will keep the device on the xStatus Peripherals ConnectedDevice list. If the
        peripheral is not set to send a heartbeat, the device will disappear from the
        list after a while. Note: Does not apply to cameras."""                
        return "xCommand Peripherals HeartBeat"

'''
Connected
Literal False, True
Limit the search to currently connected devices.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def List():                
        """Lists all currently and previously connected peripherals."""                
        return "xCommand Peripherals List"

'''
ID
Required String 1 - 100
Mac address of the ISDN Link in the format "xx:xx:xx:xx:xx:xx".
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Purge():                
        """Force unpair a video conferencing device from an ISDN Link when a connection has
        been lost. Note: You must also unpair the ISDN Link to be able to pair it to
        another video conferencing device."""                
        return "xCommand Peripherals Purge"

'''
MacAddress
Required String 1 - 1450
Enter the MAC address for the ISDN Link you wish to pair to the video conferencing device.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Pairing:
    
        def Pair():                
            """Pair an ISDN Link to a video conferencing device."""                
            return "xCommand Peripherals Pairing Pair"

'''
MacAddress
Required String 1 - 100
Enter the MAC address for the ISDN Link you wish to unpair from the video conferencing device.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Unpair():                
            """Unpair the video conferencing device from an ISDN Link, when the two have
            contact."""                
            return "xCommand Peripherals Pairing Unpair"

'''
Duration
Integer 1 - 2880 Default: 60
How long the pairing process will be active (minutes).
'''

'''
Back-end Any
User roles Admin
Products Room Series
Privacy impacting No
'''

        class PinPairing:
        
            def Start():                
                """When connecting a touch controller to a video device across the network, you can
                pair by using a PIN or a passphrase. To initiate pairing by PIN, issue this
                command."""                
                return "xCommand Peripherals Pairing PinPairing Start"

'''
Back-end Any
User roles Admin
Products Room Series
Privacy impacting No
'''

            def Stop():                
                """Stop the pin pairing process."""                
                return "xCommand Peripherals Pairing PinPairing Stop"

'''
ID
Required String 1 - 100
A unique ID for the Room Navigator that is connected to the device, typically its MAC address. Refer to the Peripherals ConnectedDevice [n] ID status.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class TouchPanel:
    
        def Configure():                
            """A Room Navigator can operate in different modes: As standard user interface for
            the video conferencing device (controller), as a room booking device (room
            scheduler), or to display a persistent web app. The information, buttons, and
            controls displayed on the Room Navigator screen depend on the mode. You can also
            add information whether the Room Navigator is in the same room as the device, or
            if it is outside the room. Information about the location is useful when
            collecting and processing senso..."""                
            return "xCommand Peripherals TouchPanel Configure"

'''
ContactMethodLimit
Integer 0 - 10 Default: 0
Limit the number of records in the result set to this number. For example, if the limit is set to 2, the ResultSet will contain only 2 entries even if the total number of hits is larger.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Phonebook:

    def Search():                
        """The search command lets you search in both the local and corporate phone books.
        A search gives a ResultSet. The total number of folders and contacts (TotalRows)
        is always included in the result set when searching the local phone book. When
        searching a corporate phonebook the total number of folders and contacts may not
        be included. Whether it is included or not depends on the backend corporate
        phonebook service (for example, CUCM, VCS, or TMS) and its version."""                
        return "xCommand Phonebook Search"

'''
CallRate
Integer 0 - 6000
Set the call rate (kbps) to use when calling this contact.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Contact:
    
        def Add():                
            """Add a new contact to the local phonebook. The command returns the ContactId,
            which is a unique string that identifies the contact; typically, the format is
            “localContactId-n”. You can add several contact methods (each with different
            Number, CallRate, CallType, Device, and Protocol) to a contact using the
            xCommand Phonebook ContactMethod Add command. Only the first contact method will
            appear in the Favorites list on the touch controller. All contact methods are
            available on the other UIs."""                
            return "xCommand Phonebook Contact Add"

'''
ContactId
Required String 0 - 255
The unique identifier for the contact. The identifier will be returned by an xCommand Phonebook Search command. It was also returned when the xCommand Phonebook Contact Add command was issued to make the contact.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Delete an existing contact from the local phonebook."""                
            return "xCommand Phonebook Contact Delete"

'''
ContactId
Required String 0 - 255
The unique identifier for the contact you want to modify. The identifier will be returned by an xCommand Phonebook Search command. It was also returned when the xCommand Phonebook Contact Add command was issued to make the contact.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Modify():                
            """Modify contact details of an existing contact in the local phonebook. The
            following parameters can be changed using this command: Name, FolderId, ImageURL
            and Title. You must use the xCommand Phonebook ContactMethod Modify command to
            change the other parameters: Number, Protocol, CallRate, CallType and Device."""                
            return "xCommand Phonebook Contact Modify"

'''
CallRate
Integer 0 - 6000
Set the call rate (kbps) to use when calling this contact.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class ContactMethod:
    
        def Add():                
            """Add contact details for an existing contact in the local phonebook. The command
            returns the ContactMethodId, which is a unique string that identifies the
            contact method; typically, the format is “n”. You can add several contact
            methods to a contact. Note that only the first contact method will appear in the
            Favorites list on the device's user interface. The first contact method may have
            been created when issuing the xCommand Phonebook Contact Add command to make the
            contact. All contact methods ..."""                
            return "xCommand Phonebook ContactMethod Add"

'''
ContactId
Required String 0 - 255
The unique identifier for the contact you want to change. The identifier will be returned by an xCommand Phonebook Search command. It was also returned when the xCommand Phonebook Contact Add command was issued to make the contact.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Delete a contact method from an existing contact in the local phonebook."""                
            return "xCommand Phonebook ContactMethod Delete"

'''
CallRate
Integer 0 - 6000
Set the call rate (kbps) to use when calling this contact.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Modify():                
            """Modify details about the contact method for an existing contact in the local
            phonebook."""                
            return "xCommand Phonebook ContactMethod Modify"

'''
Name
Required String 0 - 255
The name of the folder.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Folder:
    
        def Add():                
            """Phonebook entries can be stored in folders. Use this command to add a folder to
            the local phonebook. The command returns the FolderId, which is a unique string
            that identifies the folder; typically, the format is “localGroupId-n”."""                
            return "xCommand Phonebook Folder Add"

'''
FolderId
Required String 0 - 255
The unique identifier for the folder. The identifier will be returned by an xCommand Phonebook Search command. It was also returned when the xCommand Phonebook Folder Add command was issued to make the folder.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Delete an existing folder from the local phonebook."""                
            return "xCommand Phonebook Folder Delete"

'''
FolderId
Required String 0 - 255
The unique identifier for the folder. The identifier will be returned by an xCommand Phonebook Search command. It was also returned when the xCommand Phonebook Folder Add command was issued to make the folder.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Modify():                
            """Modify an existing phonebook folder."""                
            return "xCommand Phonebook Folder Modify"

'''
ConnectorId
IntegerArray 1 - 2
Select the video input source to be used for presentation, identified by connectorId.
'''

'''
Back-end Any
User roles Admin, User
Products Room Kit, Room Kit Mini
Privacy impacting ⚠️ Yes
'''

class Presentation:

    def Start():                
        """Open a media stream from the selected presentation source. You can combine
        multiple presentation sources in a single presentation video stream (the maximum
        number of different input sources depend on the type of video conferencing
        device) by adding multiple ConnectorId or PresentationSource parameters in the
        same command. The order in which you place them in the command determines the
        order in which the sources show up on the screen. You cannot use a mix of
        identifier types in the same command; ..."""                
        return "xCommand Presentation Start"

'''
Instance
Literal 1, 2, 3, 4, 5, 6
When you have multiple presentations running, specify which presentation instance you wish to stop. The instance number is determined when the presentation is started.
'''

'''
Back-end Any
User roles Admin, User
Products Board 55, Board 55S, Board 70, Board 70S, Board 85S, Desk Hub, Desk Mini, Room Kit, Room Kit Mini
Privacy impacting ⚠️ Yes
'''

    def Stop():                
        """Stop the media stream from the presentation source."""                
        return "xCommand Presentation Stop"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Provisioning:

    def CompleteUpgrade():                
        """Starts installing the software upgrade if you wish to install it before it is
        set to do so."""                
        return "xCommand Provisioning CompleteUpgrade"

'''
Reason
String 0 - 255
Provide information about why the upgrade was postponed.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def PostponeUpgrade():                
        """Postpones the installing of the software upgrade."""                
        return "xCommand Provisioning PostponeUpgrade"

'''
Pin
Required String 1 - 255
A valid pin code for the user, as set up in CUCM.
'''

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class CUCM:
    
        class ExtensionMobility:
        
            def Login():                
                """Login command for the Extension Mobility service. You log in to the Extension
                Mobility service with a username (UserId) and pin code (Pin). The username and
                pin code are set up in CUCM. CUCM also supports multiple profiles for a user. If
                you, for a user that has multiple profiles, submit a login command with only
                username and pin code, CUCM will send a list of available profiles back to the
                device. Then the device will create corresponding
                ExtensionMobilityProfileSelection Profile events, so tha..."""                
                return "xCommand Provisioning CUCM ExtensionMobility Login"

'''
Back-end On-prem
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Logout():                
                """This command will log you out of your Extension Mobility profile."""                
                return "xCommand Provisioning CUCM ExtensionMobility Logout"

'''
Checksum
String 0 - 128
The checksum is used to ensure the integrity of the downloaded customization template. When using HTTP, it is mandatory to add a checksum. When using HTTPS, it is mandatory to add a checksum only if you are downloading the template from a server that presents an unsigned certificate, or a self-signed certificate that is not in the CA list of the device (not trusted).
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Service:
    
        def Fetch():                
            """Add or update the customization template that details the custom elements of the
            device. Examples of custom elements are: branding images, macros, favorites,
            sign-in banner, and in-room control panels."""                
            return "xCommand Provisioning Service Fetch"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Proximity:

    class Services:
    
        def Activate():                
            """Reactivate the Proximity services that were deactivated with xCommand Proximity
            Services Deactivate."""                
            return "xCommand Proximity Services Activate"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Deactivate():                
            """This command deactivates all proximity services on the device. To reactivate
            proximity services use the command xCommand Proximity Services Activate."""                
            return "xCommand Proximity Services Deactivate"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class RoomCleanup:

    def Cancel():                
        """Cancel the scheduled daily room cleanup."""                
        return "xCommand RoomCleanup Cancel"

'''
ContentType
LiteralArray LiteralArray
The type of data to be deleted. TemporaryAccounts: Delete any temporary accounts that may be logged-in on the device (for example, a OneDrive account accessed through an Enterprise Content Management (ECM) service). Whiteboards: Delete all whiteboards on the device. WebData: Delete all web browsing data on the device.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Run():                
        """Run a cleanup of the specified type of data, as applicable."""                
        return "xCommand RoomCleanup Run"

'''
PresetId
Required Integer 1 - 15
The ID of the preset you want to activate.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class RoomPreset:

    def Activate():                
        """Activate one of the locally stored presets. Note that information about all
        video input sources, and pan, tilt, zoom and focus values for all cameras are
        included in the same preset. In contrast, the xCommand Camera Preset commands
        applies to individual cameras only."""                
        return "xCommand RoomPreset Activate"

'''
PresetId
Required Integer 1 - 15
The ID of the preset you want to delete.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Clear():                
        """Delete a preset. Note that information about all video input sources, and pan,
        tilt, zoom and focus values for all cameras are included in the same preset. In
        contrast, the xCommand Camera Preset commands applies to individual cameras
        only."""                
        return "xCommand RoomPreset Clear"

'''
Description
String 0 - 255
Enter a description of the camera preset.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Store():                
        """Store the connector selections for all video input sources and the current
        position (pan and tilt), zoom and focus values for all cameras. Note that
        information about all video input sources, and pan, tilt, zoom and focus values
        for all cameras are included in the same preset. The device may hold 15 such
        predefined video input presets. These presets are available for far end control.
        That is, they are referred in the PresetId parameter of the FarEndControl Preset
        Activate command. In contrast, t..."""                
        return "xCommand RoomPreset Store"

'''
CallHistory
Required Literal NonPersistent, Persistent
In non-persistent mode call history is deleted when the device reboots.
'''

'''
Back-end On-prem
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Security:

    def Persistency():                
        """Set the following features to persistent or non-persistent mode. In non-
        persistent mode the information gathered by the specified feature does not
        persist a reboot of the device. Persistent mode is the default. This command
        reboots the device."""                
        return "xCommand Security Persistency"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Certificates:
    
        class CA:
        
            def Add():                
                """Uploads CA security certificates to this device. This is a multiline command."""                
                return "xCommand Security Certificates CA Add"

'''
Fingerprint
Required String 0 - 128
The unique Identifier for the certificate that is deleted. You can get the fingerprint ID by running xCommand Security Certificates CA Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Delete():                
                """Deletes a CA security certificate from this device."""                
                return "xCommand Security Certificates CA Delete"

'''
Format
Literal PEM, Text Default: Text
Specifies the format of the listed certificates, PEM (Privacy Enhanced Mail) or plain text.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Show():                
                """Shows the details for the CA security certificates on this device."""                
                return "xCommand Security Certificates CA Show"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class CUCM:
        
            class CTL:
            
                def Delete():                
                    """api-description all="true">Deletes the Certificate Trust List (CTL) and Identity
                    Trust List (ITL) from this device. This command applies only to devices that are
                    registered to CUCM."""                
                    return "xCommand Security Certificates CUCM CTL Delete"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

                def Show():                
                    """Shows the details of the Certificate Trust List (CTL) on this device. CTL is
                    used for devices that are registered to CUCM and contains a list of certificates
                    for services within the CUCM cluster that the device is to trust."""                
                    return "xCommand Security Certificates CUCM CTL Show"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            class ITL:
            
                def Show():                
                    """Shows the details of the Identity Trust List (ITL) on this device. ITL is used
                    for devices that are registered to CUCM and contains a list of certificates for
                    services within the CUCM cluster that the device is to trust."""                
                    return "xCommand Security Certificates CUCM ITL Show"

'''
Format
Literal PEM, Text Default: PEM
Specifies the format of the listed certificate, PEM (Privacy Enhanced Mail) or plain text.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            class MIC:
            
                def Show():                
                    """Shows the details of the Manufacture Installed Certificate (MIC) on this device.
                    A MIC is signed by the Cisco Manufacturing CA and is installed on the device
                    during production. This certificate is immutable."""                
                    return "xCommand Security Certificates CUCM MIC Show"

'''
Fingerprint
Required String 0 - 1024
The unique identifier (ID) for the certificate that is activated. You can get the fingerprint ID by running xCommand Security Certificates Services Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class Services:
        
            def Activate():                
                """Activates a security certificate on this device."""                
                return "xCommand Security Certificates Services Activate"

'''
PrivateKeyPassword
String 0 - 128
Stores the details of the private key for the password.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Add():                
                """Uploads security certificates to this device. This is a multiline command."""                
                return "xCommand Security Certificates Services Add"

'''
Fingerprint
Required String 0 - 1024
The unique Identifier for the certificate that is deactivated. You can get the fingerprint ID by running xCommand Security Certificates Services Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Deactivate():                
                """Deactivates security certificates on this device."""                
                return "xCommand Security Certificates Services Deactivate"

'''
Fingerprint
Required String 0 - 128
The unique Identifier for the certificate that is deleted. You can get the fingerprint ID by running xCommand Security Certificates Services Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Delete():                
                """Deletes security certificates from this device."""                
                return "xCommand Security Certificates Services Delete"

'''
Filter
Literal 802.1X, HTTPS, Audit, SIP, Pairing, WebexIdentity, HttpClient
Filters the results according to the chosen service. 802.1X: For applying 802.1x security authentication. Audit: For performing external audit logging. HTTPS: For applying HTTPS security authentication. HttpClient: For use with Mutual TLS authentication when using the xcommand HttpClient API. Pairing: For pairing touch devices that are not directly connected to the endpoint. SIP: For applying SIP security authentication. WebexIdentity: For identifying the device in end-to-end encryption scenarios on the Cisco Webex cloud.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Show():                
                """Shows details for security certificates on this device."""                
                return "xCommand Security Certificates Services Show"

'''
Fingerprint
Required String 0 - 128
The unique Identifier for the certificate that is disabled. You can get the fingerprint ID by running xCommand Security Certificates Services Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class ThirdParty:
        
            def Disable():                
                """Disables a bundled certificate used for SMTP and HttpClient. Disabling a
                certificate results in a server providing a certificate signed with this root
                certificate will be declined."""                
                return "xCommand Security Certificates ThirdParty Disable"

'''
Fingerprint
Required String 0 - 128
The unique Identifier for the certificate that is enabled. You can get the fingerprint ID by running xCommand Security Certificates Services Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Enable():                
                """Enables a bundled certificate used for SMTP and HttpClient."""                
                return "xCommand Security Certificates ThirdParty Enable"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def List():                
                """Lists all bundled certificates and their state."""                
                return "xCommand Security Certificates ThirdParty List"

'''
Fingerprint
Required String 0 - 128
The unique Identifier for the certificate you want to see. You can get the fingerprint ID by running xCommand Security Certificates Services Show.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Show():                
                """Shows a single third-party certificate."""                
                return "xCommand Security Certificates ThirdParty Show"

'''
Filter
Literal Cisco, Non-Cisco, TLS-proxy
Cisco: Shows the list of CA certificates used when communicating with servers and services that are provided by Cisco. Non-Cisco: Shows the list CA certificates used when communicating with servers and services that are provided by others than Cisco. TLS-proxy: Shows the list of additional CA certificates required when using a TLS inspecting proxy for outbound traffic.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class Webex:
        
            def Show():                
                """This command applies only to devices that are registered to the Cisco Webex
                cloud service. Shows the list of trusted CA certificates that verifies the
                certificates of servers and services used by the Cisco Webex cloud."""                
                return "xCommand Security Certificates Webex Show"

'''
Filter
Literal Internal, External
Internal: Shows the list of internal certificate authorities. External: Shows a list of external certificate authorities.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class WebexIdentity:
        
            def Show():                
                """This command applies only to devices that are registered to the Cisco Webex
                cloud service. Shows the root Certificate Authority (CA) list for Webex
                Identity."""                
                return "xCommand Security Certificates WebexIdentity Show"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Ciphers:
    
        def List():                
            """List the ciphers supported by various services (domains). Result: Name: Name of
            this domain. * Syslog-TLS: Used for logging over TLS. * HTTPS server: Used by
            the endpoint's own web server. * HTTPS client: Used for all https client traffic
            from the endpoint. * Pairing: Used for peripheral pairing to touch devices and
            microphones/amplifiers. * SIP TLS: Used for direct IP SIP connections, SIP
            connections to CUCM or to VCS or other SIP proxies when transport is TLS.
            Cipherlist: The actual ..."""                
            return "xCommand Security Ciphers List"

'''
Secret
Required String 0 - 1024
First time: Supply a base64url encoded plain text value. Thereafter: Supply a JWE blob containing the new secret encrypted by the old secret.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class ClientSecret:
    
        def Populate():                
            """This command applies only to devices that are registered to the Cisco Webex
            cloud service. Accepts a base64url encoded plain text value for seeding the
            client secret on the device for the first time. To update the secret after that
            first time, you must supply a JWE blob containing the new secret encrypted by
            the old secret. This is a multiline command."""                
            return "xCommand Security ClientSecret Populate"

'''
Back-end Any
User roles Admin, Audit, Integrator, PairedUser, RoomControl, TouchUser, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Session:
    
        def Get():                
            """Shows details of your current session."""                
            return "xCommand Security Session Get"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def List():                
            """List active sessions."""                
            return "xCommand Security Session List"

'''
SessionId
Required String 0 - 32
The session ID number.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Terminate():                
            """Terminate a session."""                
            return "xCommand Security Session Terminate"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Standby:

    def Activate():                
        """Set the device in standby mode, which turns off the video outputs and put the
        camera into sleep mode."""                
        return "xCommand Standby Activate"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Deactivate():                
        """Bring the device out of standby mode."""                
        return "xCommand Standby Deactivate"

'''
Back-end Any
User roles Admin, Integrator
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def Halfwake():                
        """Sets the device to "Halfwake" state. This state informs the user from the UI, to
        pick up a remote or to tap the touch device to get started."""                
        return "xCommand Standby Halfwake"

'''
Delay
Required Integer 1 - 480
Set the delay in minutes.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def ResetHalfwakeTimer():                
        """Sets a temporary Halfwake timer delay. If the device is in Halfwake mode when
        the reset timer is set, the device is brought out of Halfwake mode. When left
        idle for the given delay the device goes into halfwake mode."""                
        return "xCommand Standby ResetHalfwakeTimer"

'''
Delay
Integer 1 - 480
Set the delay in minutes.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def ResetTimer():                
        """Reset the standby delay timer or set a temporary standby delay. If the device is
        in standby mode when the timer is set, the device is brought out of standby mode
        before starting the countdown. If you don't specify a Delay, the standby delay
        timer is reset, and the device goes into standby after the period that is given
        by the Standby Delay setting (xConfiguration Standby Delay). If you do specify a
        Delay, the device goes into standby when it has been idle for the specified
        period. Next time, the..."""                
        return "xCommand Standby ResetTimer"

'''
Action
Literal Restart, Shutdown Default: Restart
As a default the device restarts after a reboot. By selecting Shutdown, the device will not restart.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class SystemUnit:

    def Boot():                
        """Reboot the device."""                
        return "xCommand SystemUnit Boot"

'''
Confirm
Required Literal Yes
Include to confirm your choice.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def FactoryReset():                
        """Reset the codec to factory default settings. The call logs are deleted and all
        device parameters are reset to default values. All files that have been uploaded
        to the codec are deleted. Option key(s) are not affected. Use the parameter Keep
        in order to choose which configurations and files to keep when you factory reset
        the device. As a default the device restarts after the factory reset, but other
        behaviors can be forced by selecting a different TrailingAction."""                
        return "xCommand SystemUnit FactoryReset"

'''
Confirm
Required Literal Yes
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def SoftReset():                
        """Reset most parameters to their default values. This does not include parameters
        associated with room setup, such as camera position, language, and volume."""                
        return "xCommand SystemUnit SoftReset"

'''
Forced
Literal False, True Default: True
You can force a device to accept a software upgrade immediately, without giving users a chance to acknowledge or postpone the update.
'''

'''
Back-end Any
User roles Admin, TouchUser
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    def SoftwareUpgrade():                
        """Initiate a software upgrade by fetching the software from a given URL."""                
        return "xCommand SystemUnit SoftwareUpgrade"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class DeveloperPreview:
    
        def Activate():                
            """Activate developer preview mode. When developer preview mode is activated and
            you have a DeveloperPreview option key installed, you will get access to public-
            api-preview xAPI nodes."""                
            return "xCommand SystemUnit DeveloperPreview Activate"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Deactivate():                
            """Deactivate developer preview mode."""                
            return "xCommand SystemUnit DeveloperPreview Deactivate"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class FirstTimeWizard:
    
        def Stop():                
            """Stops the wizard which appears the first time you start the device, so the
            device can be set up without it. The wizard only appears again if the device is
            reset to its factory default settings."""                
            return "xCommand SystemUnit FirstTimeWizard Stop"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Notifications:
    
        def RemoveAll():                
            """Clears the list of system notifications that are reported by xStatus SystemUnit
            Notifications Text/Type."""                
            return "xCommand SystemUnit Notifications RemoveAll"

'''
Key
Required String 16 - 24
The key you have received for the option you wish to switch on.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class OptionKey:
    
        def Add():                
            """Add an option key to support additional features."""                
            return "xCommand SystemUnit OptionKey Add"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def List():                
            """List all option keys."""                
            return "xCommand SystemUnit OptionKey List"

'''
Type
Required Literal Encryption, MultiSite, RemoteMonitoring, DeveloperPreview
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Remove():                
            """Remove a specified option key."""                
            return "xCommand SystemUnit OptionKey Remove"

'''
Confirm
Required Literal Yes
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def RemoveAll():                
            """Remove all option keys."""                
            return "xCommand SystemUnit OptionKey RemoveAll"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class SignInBanner:
    
        def Clear():                
            """Clear the sign in banner set with xCommand SystemUnit SignInBanner Set."""                
            return "xCommand SystemUnit SignInBanner Clear"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Get():                
            """Get the custom message set with xCommand SystemUnit SignInBanner Set."""                
            return "xCommand SystemUnit SignInBanner Get"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Set():                
            """Set a sign in banner with a custom message on the device's user interface. This
            is a multiline command. Use: xCommand SystemUnit SignInBanner Set <enter> Banner
            text <enter> . <enter>"""                
            return "xCommand SystemUnit SignInBanner Set"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class WelcomeBanner:
    
        def Clear():                
            """Clear the welcome banner set with xCommand SystemUnit WelcomeBanner Set."""                
            return "xCommand SystemUnit WelcomeBanner Clear"

'''
Back-end Any
User roles Admin, Audit, Integrator, PairedUser, RoomControl, TouchUser, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Get():                
            """Get the custom message set with xCommand SystemUnit WelcomeBanner Set."""                
            return "xCommand SystemUnit WelcomeBanner Get"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Set():                
            """Set up a welcome banner that the user sees after they sign in to the device's
            web interface or the command line interface. The banner can for example contain
            information that the user needs to get started or things they need to be aware
            of when changing settings. This is a multiline command. Use: xCommand SystemUnit
            WelcomeBanner Set <enter> Banner text <enter> . <enter>"""                
            return "xCommand SystemUnit WelcomeBanner Set"

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Time:

    class DateTime:
    
        def Get():                
            """Read the time and date from the device."""                
            return "xCommand Time DateTime Get"

'''
Day
Integer 1 - 31
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Set():                
            """Set the date and time for the device, if not available from NTP (Network Time
            Protocol)."""                
            return "xCommand Time DateTime Set"

'''
Back-end Any
User roles Admin, Integrator
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class UserInterface:

    class Branding:
    
        def Clear():                
            """Deletes the custom wallpaper, the brand background image, and the logo files
            from the device."""                
            return "xCommand UserInterface Branding Clear"

'''
Type
Required Literal Background, Branding, HalfwakeBackground, HalfwakeBranding
Background: Delete the custom wallpaper. Branding: Delete the logo that is displayed when the device is active. HalfwakeBackground: Delete the brand image that is displayed as a background when the device is in the halfwake state. HalfwakeBranding: Delete the logo that is displayed when the device is in the halfwake state.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Deletes the image file, which is specified in the Type parameter, from the
            device."""                
            return "xCommand UserInterface Branding Delete"

'''
Checksum
String 0 - 128
Specify the checksum for the image file that is to be fetched. The checksum is used to ensure the integrity of the downloaded image file. When using HTTP, it is mandatory to add a checksum. When using HTTPS, it is mandatory to add a checksum only if you are downloading the template from a server that presents an unsigned certificate, or a self-signed certificate that is not in the CA list of the device (not trusted).
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Fetch():                
            """Fetches an image file from a URL and stores the file on the device. Supply the
            URL first. The following image formats are supported: BMP, GIF, JPEG, and PNG.
            The maximum image size is 16 megapixels, and the maximum file size is 8MB. The
            Type parameter determines what kind of image it is. If it is a background image,
            the associated feature (Custom wallpaper or Branding with background and logo)
            is automatically applied. This command issues an HTTP request, so it is included
            in the HTTP requests c..."""                
            return "xCommand UserInterface Branding Fetch"

'''
Size
Literal Large, Small, Thumbnail Default: Large
Large: The size of the image that is displayed on the main screen. Small: The size of the image that is displayed on the touch controller. Thumbnail: The size of the image that is used in the web interface illustrations.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Get():                
            """The command returns the image file that is specified in the Type parameter,
            given that such a file is stored on the device. The file is Base64 encoded. The
            format is JPG for background images and PNG for logos, regardless of the format
            of the originally uploaded file. Background images are stored in three sizes,
            one for the main screen, one for the touch controller, and one for the web
            interface illustrations. Use the Size parameter to choose which one to get.
            Logos have only one size."""                
            return "xCommand UserInterface Branding Get"

'''
Type
Required Literal Background, Branding, HalfwakeBackground, HalfwakeBranding
Background: A new background image that can be used as a custom wallpaper is ready for use. Branding: A new logo that can be displayed when the device is active is ready for use. HalfwakeBackground: A new brand image that can be displayed as a background when the device is in the halfwake state is ready for use. HalfwakeBranding: A new logo that can be displayed when the device is in the halfwake state is ready for use.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Updated():                
            """This command creates an event that tells that a new image file is uploaded to
            the device and ready for use. The Type parameter identifies what kind of image
            it is."""                
            return "xCommand UserInterface Branding Updated"

'''
CustomId
String 0 - 128
Specify a custom identifier for this image. You can get the CustomId for the images used by using xStatus UserInterface Branding CustomId.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Upload():                
            """Uploads an image file to the device. The following image formats are supported:
            BMP, GIF, JPEG, and PNG, and the maximum image size is 16 megapixels. The file
            must be Base64 encoded, and the maximum file size is 4 MByte. The Type parameter
            specifies the usage of the image. If it is a background image, the associated
            feature (Custom wallpaper or Branding with background and logo) is automatically
            applied. This is a multiline command."""                
            return "xCommand UserInterface Branding Upload"

'''
ActivityType
Literal Custom
Custom: Custom buttons, panels, and widgets are removed.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Room Series
Privacy impacting ⚠️ Yes
'''

    class Extensions:
    
        def Clear():                
            """Delete user interface extensions (custom buttons, panels, and widgets) from the
            device. If you don't specify an ActivityType, all extensions are deleted."""                
            return "xCommand UserInterface Extensions Clear"

'''
EmbedData
Literal On, Off
Off: Do not embed the base64-encoded icons in the XML output. On: Embed the base64-encoded icons icons in the output.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Export():                
            """Export the UserInterface Extensions as the XML result of this command. This
            gives the same result as extracting through the local web interface, but it can
            be used programmatically."""                
            return "xCommand UserInterface Extensions Export"

'''
ActivityType
Literal Custom
Custom: Custom buttons, panels, and widgets are listed.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Room Series
Privacy impacting ⚠️ Yes
'''

        def List():                
            """List user interface extensions (custom buttons, panels, and widgets) that exist
            on the device. If you don't specify an ActivityType, all extensions are listed."""                
            return "xCommand UserInterface Extensions List"

'''
ConfigId
Required String 0 - 40
The unique identifier for the configuration.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Set():                
            """Set the configuration scheme you have chosen in the user interface extensions
            (widgets) for your device. Updates the UserInterface Extensions status tree.
            This is a multiline command."""                
            return "xCommand UserInterface Extensions Set"

'''
Id
Required String 0 - 128
The id of the icon to be deleted.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class Icon:
        
            def Delete():                
                """Delete an icon from the device's list of UI extension icons. Specify the id of
                the icon to be deleted. You can use xCommand UserInterface Extensions Icon List
                to get a list of all the icons with ids. If you are not sure which icon is the
                one you are looking for, you can use xcommand UserInterface Icon Get to get the
                base64-encoded value and use an internet tool to decode base64 to image."""                
                return "xCommand UserInterface Extensions Icon Delete"

'''
Filter
Literal All, Unused Default: All
All: Delete all the UI extensions icons. Unused: Delete only the icons that are not used by a UI extension.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def DeleteAll():                
                """Delete all or a subset of UI extensions icons."""                
                return "xCommand UserInterface Extensions Icon DeleteAll"

'''
Url
Required String 0 - 2048
The URL for the icon.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Download():                
                """Download an icon from the specified URL and save it as a UI Extensions icon on
                the device."""                
                return "xCommand UserInterface Extensions Icon Download"

'''
Url
Required String 0 - 2048
The URL for the website you want to look for and attempt to download a suitable icon.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Fetch():                
                """Search a website for a representative icon and download this to the device for
                use with web apps and other UI extensions."""                
                return "xCommand UserInterface Extensions Icon Fetch"

'''
Id
Required String 0 - 128
The unique identifier corresponding to the icon.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Get():                
                """Get a base64-encoded representation of the UI Extensions icon with the specified
                Id. If you want to see the image, you can use an internet tool to decode base64
                to image. Use xCommand UserInterface Extensions Icon List to get a list of all
                the icon Ids."""                
                return "xCommand UserInterface Extensions Icon Get"

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def List():                
                """Get a list of the unique identifiers for all the UI extension icons on the
                device."""                
                return "xCommand UserInterface Extensions Icon List"

'''
Id
String 0 - 128
A custom unique identifier corresponding to the icon.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Upload():                
                """Upload an icon image for use by UI extensions on the device. This is a multiline
                command. Provide a base64-encoded version of an image."""                
                return "xCommand UserInterface Extensions Icon Upload"

'''
PanelId
Required String 0 - 255
The unique identifier of the custom panel.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class Panel:
        
            def Clicked():                
                """Creates an event when the user clicks a custom panel."""                
                return "xCommand UserInterface Extensions Panel Clicked"

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Close():                
                """Closes an open custom panel."""                
                return "xCommand UserInterface Extensions Panel Close"

'''
PageId
String 0 - 255
The unique identifier of a page on a custom panel.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Open():                
                """Opens the custom panel that has the given PanelId. If the panel has multiple
                pages you can specify which page to open by including the PageId parameter."""                
                return "xCommand UserInterface Extensions Panel Open"

'''
PanelId
Required String 0 - 255
The unique identifier of the custom panel.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Remove():                
                """Removes the custom panel from the user interface of this device."""                
                return "xCommand UserInterface Extensions Panel Remove"

'''
PanelId
Required String 1 - 255
The unique identifier of the custom panel.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Save():                
                """Adds a custom panel to the current configuration. The panel will be added to the
                configuration, but if a panel with the same panel ID already exists, it will be
                overwritten. This is a multiline command."""                
                return "xCommand UserInterface Extensions Panel Save"

'''
Color
String 0 - 255
The color of the specified panel button, specified in hexadecimal (for example, #4287f5).
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Update():                
                """Updates the custom panel that has the given PanelId. Successful changes are
                immediately visible on the endpoint."""                
                return "xCommand UserInterface Extensions Panel Update"

'''
Type
String 0 - 255
The type of widget that is set.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class Widget:
        
            def Action():                
                """Sets the action of the given widget. Updates the UserInterface Extensions status
                tree."""                
                return "xCommand UserInterface Extensions Widget Action"

'''
Value
Required String 0 - 255
The value of the widget. The range of values depends on the widget type.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def SetValue():                
                """Set the value of the given widget. Updates the UserInterface Extensions status
                tree. Returns an error if the value is out of range."""                
                return "xCommand UserInterface Extensions Widget SetValue"

'''
WidgetId
Required String 0 - 255
The unique identifier for the widget.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def UnsetValue():                
                """Empties the value of the given widget. Updates the UserInterface Extensions
                status tree and notifies the user interface that this widget is no longer
                selected."""                
                return "xCommand UserInterface Extensions Widget UnsetValue"

'''
Color
Required Literal Green, Yellow, Red, Off
Off: Turn the LED lights off. Green/Red/Yellow: Turn on the LED lights with the specified color.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class LedControl:
    
        class Color:
        
            def Set():                
                """The wall mount version of the Room Navigator has LED lights. Use this command to
                specify the color and turn the LED lights on or off. The UserInterface
                LedControl Mode setting must be Manual for this command to have any effect."""                
                return "xCommand UserInterface LedControl Color Set"

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Message:
    
        class Alert:
        
            def Clear():                
                """Remove the message which was displayed using the UserInterface Message Alert
                Display command. This is required when the Duration parameter is not set."""                
                return "xCommand UserInterface Message Alert Clear"

'''
Duration
Integer 0 - 3600 Default: 0
How long (in seconds) the message is to be displayed on the screen. If set to 0 (zero) the message is displayed until a UserInterface Message Alert Clear command is sent.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Display():                
                """Display a message on screen. Optionally you can keep the message for a specified
                duration of time. If Duration is not set, the command must be followed by a
                UserInterface Message Alert Clear command."""                
                return "xCommand UserInterface Message Alert Display"

'''
FeedbackId
String 0 - 255
The FeedbackId corresponds to the FeedbackId given by the UserInterface Message Prompt Display command.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class Prompt:
        
            def Clear():                
                """Remove the window which was displayed using the UserInterface Message Prompt
                Display command. This is required when the Duration parameter is not set. Use
                the xFeedback commands to monitor the feedback from the user. Read more about
                the xFeedback commands in the API introduction section in this guide."""                
                return "xCommand UserInterface Message Prompt Clear"

'''
Duration
Integer 0 - 3600 Default: 0
How long (in seconds) the message window is to be displayed on the screen. If set to 0 (zero) the message window is displayed until a UserInterface Message Prompt Clear command is sent.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Display():                
                """Display a small window on screen with a title, text and up to five options for
                response from the user. The message is displayed on screen until the user gives
                a response, or until the device receives a UserInterface Message Prompt Clear
                command. Use the xFeedback commands to monitor the feedback from the user. Read
                more about the xFeedback commands in the API introduction section in this guide."""                
                return "xCommand UserInterface Message Prompt Display"

'''
FeedbackId
String 0 - 255
The FeedbackId corresponds to the FeedbackId given by the UserInterface Message Prompt Display command.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Response():                
                """Give a response to the UserInterface Message Prompt Display command. This
                command is executed when the user selects an option in the user interface. Use
                the xFeedback commands to monitor the feedback from the user. Read more about
                the xFeedback commands in the API introduction section in this guide."""                
                return "xCommand UserInterface Message Prompt Response"

'''
FeedbackId
String 0 - 255
The FeedbackId corresponds to the FeedbackId given by the UserInterface Message Rating Display command. If the FeedbackId is not given, all UserInterface Message Rating windows will be closed.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class Rating:
        
            def Clear():                
                """Remove the message which was displayed using the UserInterface Message Rating
                Display command. This is required when the Duration parameter is not set."""                
                return "xCommand UserInterface Message Rating Clear"

'''
Duration
Integer 0 - 3600 Default: 0
How long (in seconds) the message window is to be displayed on the screen. If empty or set to 0, the message window is displayed until a UserInterface Message Rating Clear command is sent.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Display():                
                """Display a small window on screen with a title and text. Rating stars are
                provided for the user to select. The message is displayed on screen until the
                user gives a response, or until the device receives a UserInterface Message
                Rating Clear command. Use the xFeedback commands to monitor the feedback from
                the user. Read more about the xFeedback commands in the API introduction section
                in this guide."""                
                return "xCommand UserInterface Message Rating Display"

'''
FeedbackId
String 0 - 255
The FeedbackId corresponds to the FeedbackId given by the UserInterface Message Rating Display command.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Response():                
                """Give a response to the UserInterface Message Rating Display command. This
                command is executed when the user selects an option in the user interface. Use
                the xFeedback commands to monitor the feedback from the user. Read more about
                the xFeedback commands in the API introduction section in this guide."""                
                return "xCommand UserInterface Message Rating Response"

'''
FeedbackId
String 0 - 255
The FeedbackId corresponds to the FeedbackId given by the UserInterface Message TextInput Display command.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class TextInput:
        
            def Clear():                
                """Remove the text input message which was displayed using the UserInterface
                Message TextInput Display command. This is required when the Duration parameter
                is not set. Use the xFeedback commands to monitor the feedback from the user.
                Read more about the xFeedback commands in the API introduction section in this
                guide."""                
                return "xCommand UserInterface Message TextInput Clear"

'''
Duration
Integer 0 - 3600 Default: 0
How long (in seconds) the message is to be displayed on the screen. If set to 0 (zero) the message is displayed until a UserInterface Message TextInput Clear command is sent.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Display():                
                """Displays an input dialog box to which a user can respond. This is only supported
                for devices with a touch-based user interface. The message is displayed on
                screen until the user gives a response, or until the device receives a
                UserInterface Message TextInput Clear command. Use the xFeedback commands to
                monitor the feedback from the user. Read more about the xFeedback commands in
                the API introduction section in this guide."""                
                return "xCommand UserInterface Message TextInput Display"

'''
FeedbackId
String 0 - 255
To identify the feedback enter a FeedbackId.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Response():                
                """Give a response to the UserInterface Message TextInput Display command. This
                command is executed when the user submits the reply that he has entered in the
                text input field in the user interface. Use the xFeedback commands to monitor
                the feedback from the user. Read more about the xFeedback commands in the API
                introduction section in this guide."""                
                return "xCommand UserInterface Message TextInput Response"

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class TextLine:
        
            def Clear():                
                """Remove the text line which was displayed by the UserInterface Message TextLine
                Display command. This is required when the Duration parameter is not set."""                
                return "xCommand UserInterface Message TextLine Clear"

'''
Duration
Integer 0 - 3600 Default: 0
How long (in seconds) the text line is to be displayed on the screen. If set to 0 (zero) the text line is displayed until a UserInterface Message TextLine Clear command is sent.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Display():                
                """Display a text line on screen. Optionally you can place the text line at a
                specified location and for a specified duration of time. If Duration is not set,
                the command must be followed by the UserInterface Message TextLine Clear
                command."""                
                return "xCommand UserInterface Message TextLine Display"

'''
ConnectorId
Required Integer 1 - 2
The ID of the device connector that the external switch is connected to.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Room Kit, Room Kit Mini
Privacy impacting No
'''

    class Presentation:
    
        class ExternalSource:
        
            def Add():                
                """Establish and set up an input source that is connected to the device via an
                external switch."""                
                return "xCommand UserInterface Presentation ExternalSource Add"

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Room Series
Privacy impacting No
'''

            def List():                
                """Returns the current list of external input sources."""                
                return "xCommand UserInterface Presentation ExternalSource List"

'''
SourceIdentifier
Required String 0 - 40
The unique string that identifies this input source. It was defined when the source was created with the UserInterface Presentation ExternalSource Add command.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Room Series
Privacy impacting No
'''

            def Remove():                
                """Remove the input source (specified by the SourceIdentifier) from the list of
                external input sources."""                
                return "xCommand UserInterface Presentation ExternalSource Remove"

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Room Series
Privacy impacting No
'''

            def RemoveAll():                
                """Remove all input sources from the list of external input sources."""                
                return "xCommand UserInterface Presentation ExternalSource RemoveAll"

'''
SourceIdentifier
Required String 0 - 40
The unique string that identifies this input source. It was defined when the source was created with the UserInterface Presentation ExternalSource Add command.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl, User
Products Room Series
Privacy impacting No
'''

            def Select():                
                """Starts to present the input source (specified by the SourceIdentifier) if it is
                in Ready state (see the UserInterface Presentation ExternalSource State Set
                command). The input source will be shown in the user interface sharetray as
                "Presenting"."""                
                return "xCommand UserInterface Presentation ExternalSource Select"

'''
ErrorReason
String 0 - 80
This string is displayed in the user interface sharetray, given that the State parameter is set to Error.
'''

'''
Back-end Any
User roles Admin, Integrator, RoomControl
Products Room Series
Privacy impacting No
'''

            class State:
            
                def Set():                
                    """Set or change the state of the input source (specified by the SourceIdentifier)."""                
                    return "xCommand UserInterface Presentation ExternalSource State Set"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Translation:
    
        class Override:
        
            def Clear():                
                """Clear all translation overrides."""                
                return "xCommand UserInterface Translation Override Clear"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Get():                
                """Returns the translation override information in JSON format. If no translation
                override is set, it will return an error."""                
                return "xCommand UserInterface Translation Override Get"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Set():                
                """Set a translation override for text on the user interface. For instance, change
                the title "Whiteboard" to "whiteboard collection", or whatever you like. This is
                a multiline command that expects the override set in JSON format. For example: {
                "version": 1, "translations": [ { "sourceText": "Whiteboard", "translated":
                "WB", "language": "English" } ] } sourceText: The English version of the text to
                be replaced. translated: The text to use as the replacement for the language
                th..."""                
                return "xCommand UserInterface Translation Override Set"

'''
Back-end Any
User roles Admin
Products Codec Plus, Codec Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

    class WallpaperBundle:
    
        def Clear():                
            """Not applicable in this release."""                
            return "xCommand UserInterface WallpaperBundle Clear"

'''
Back-end Any
User roles Admin
Products Codec Plus, Codec Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def List():                
            """Not applicable in this release."""                
            return "xCommand UserInterface WallpaperBundle List"

'''
Name
Required String 0 - 255
The name of the wallpaper bundle.
'''

'''
Back-end Any
User roles Admin
Products Codec Plus, Codec Pro, Room 55, Room Kit, Room Kit Mini
Privacy impacting No
'''

        def Set():                
            """Not applicable in this release."""                
            return "xCommand UserInterface WallpaperBundle Set"

'''
Target
Literal OSD, Controller, PersistentWebApp
Controller: Only for Cisco internal use. OSD: Close the web view that is displayed on the screen of the device. PersistentWebApp: Only for Cisco internal use.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Room Series
Privacy impacting No
'''

    class WebView:
    
        def Clear():                
            """Closes the web view."""                
            return "xCommand UserInterface WebView Clear"

'''
Header
StringArray 0 - 8192
An HTTP header field. You can add up 15 Header parameters in one command, each holding one HTTP header field.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Room Series
Privacy impacting No
'''

        def Display():                
            """Opens the web view and displays the web page given by the URL."""                
            return "xCommand UserInterface WebView Display"

'''
ExpiryDays
Integer 1 - 31
Define the duration for the passphrase validity. Default is 7 days.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class UserManagement:

    class RemoteSupportUser:
    
        def Create():                
            """Create a remote support user passphrase that Technical Assistance Center (TAC)
            can use to access the device for troubleshooting."""                
            return "xCommand UserManagement RemoteSupportUser Create"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Delete the remote support user created with the command xCommand UserManagement
            RemoteSupportUser Create."""                
            return "xCommand UserManagement RemoteSupportUser Delete"

'''
Confirm
Required Literal Yes
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def DisablePermanently():                
            """Disable the creation of new remote support users. To enable the remote support
            user again you must factory reset your device."""                
            return "xCommand UserManagement RemoteSupportUser DisablePermanently"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def GetState():                
            """Retrieves the state of the generated remote support user, if one exists."""                
            return "xCommand UserManagement RemoteSupportUser GetState"

'''
Active
Literal False, True
Specifies whether this is an active user or not.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class User:
    
        def Add():                
            """Adds a new user to this device."""                
            return "xCommand UserManagement User Add"

'''
Username
Required String 0 - 127
The username of the user that will be deleted.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Delete():                
            """Deletes a user from this device."""                
            return "xCommand UserManagement User Delete"

'''
ClientCertificateDN
String 0 - 255
Identifies a user who logs in with a client certificate instead of a username and password.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Get():                
            """Shows the details of a user on this device. You must supply either a Username or
            ClientCertificateDN to identify the user."""                
            return "xCommand UserManagement User Get"

'''
Limit
Integer 0 - 65536 Default: 0
Limits the number of users that are shown to this number. 0 means no limit, i.e, all users are listed.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def List():                
            """Shows the list of users on this device."""                
            return "xCommand UserManagement User List"

'''
Active
Literal False, True
Specifies whether this is an active user or not.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Modify():                
            """Modifies the details of a particular user."""                
            return "xCommand UserManagement User Modify"

'''
Username
Required String 0 - 127
The username of the user that will be unblocked.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        def Unblock():                
            """Unblocks a user who is blocked out because of too many failed login attempts."""                
            return "xCommand UserManagement User Unblock"

'''
NewPassphrase
Required String 0 - 255
The passphrase you are changing to (new).
'''

'''
Back-end Any
User roles Admin, Audit, Integrator, PairedUser, RoomControl, TouchUser, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class Passphrase:
        
            def Change():                
                """Change the passphrase for the user you are logged in as. If you are logged in as
                the administrator, this will change the administrator passphrase."""                
                return "xCommand UserManagement User Passphrase Change"

'''
NewPassphrase
Required String 0 - 255
The passphrase you are changing to (new).
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

            def Set():                
                """Set a passphrase for the specified user. You must be logged in as an
                administrator to set a user's passphrase."""                
                return "xCommand UserManagement User Passphrase Set"

'''
Position
Required Literal CenterLeft, CenterRight, LowerLeft, LowerRight, UpperCenter, UpperLeft, UpperRight, DockLowerLeft, DockCenterLeft
Select one of the predefined positions.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class Video:

    class ActiveSpeakerPIP:
    
        def Set():                
            """Sets position for the active speakers PiP (picture in picture)."""                
            return "xCommand Video ActiveSpeakerPIP Set"

'''
ConnectorId
Required Integer 2 - 2
The unique identifier of the connector.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Room Kit, Room Kit Mini
Privacy impacting ⚠️ Yes
'''

    class CEC:
    
        class Input:
        
            def KeyClick():                
                """Mimics a remote control key click event from the input device."""                
                return "xCommand Video CEC Input KeyClick"

'''
ConnectorId
Required Integer 1 - 3
The unique identifier of the connector.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Room Series
Privacy impacting ⚠️ Yes
'''

        class Output:
        
            def KeyClick():                
                """Mimics a remote control key click event from this device."""                
                return "xCommand Video CEC Output KeyClick"

'''
ConnectorId
Integer 1 - 3
The unique identifier of the connector.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Room Series
Privacy impacting ⚠️ Yes
'''

            def SendActiveSourceRequest():                
                """A request from the video conferencing device to become the active source of the
                screen (device) that is connected to the specified output connector."""                
                return "xCommand Video CEC Output SendActiveSourceRequest"

'''
ConnectorId
Integer 1 - 3
The unique identifier of the connector.
'''

'''
Back-end Any
User roles Admin, Integrator
Products Codec Plus, Codec Pro, Room 55, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Panorama
Privacy impacting ⚠️ Yes
'''

            def SendInactiveSourceRequest():                
                """A request from the video conferencing device to stop being the active source of
                the screen (device) that is connected to the specified output connector. It is
                up to the screen to decide how to respond to the request. It can become the
                active source itself, make another source the active one, or do nothing."""                
                return "xCommand Video CEC Output SendInactiveSourceRequest"

'''
Target
LiteralArray LiteralArray
Specify from where to remove the text string. Choose between the local output, the main video stream, and the presentation stream.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Codec Plus, Codec Pro, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Kit Mini, Room Panorama
Privacy impacting No
'''

    class Graphics:
    
        def Clear():                
            """Remove a text string that has been added to the main video stream, the
            presentation stream, or the local output using the Video Graphics Text Display
            command. If you don't want to remove the text string from all those places, you
            can use multiple Target parameters to choose a subset."""                
            return "xCommand Video Graphics Clear"

'''
Date
Literal On, Off
Specify whether to include the date in the text string.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Codec Plus, Codec Pro, Room 55 Dual, Room 70 Dual, Room 70 Dual G2, Room 70 Panorama, Room 70 Single, Room 70 Single G2, Room Kit, Room Kit Mini, Room Panorama
Privacy impacting No
'''

        class Text:
        
            def Display():                
                """Compose a text string that will be added to the main video stream, the
                presentation stream, and the local output. If you don't want to add the text
                string all those places, you can use multiple Target parameters to choose a
                subset."""                
                return "xCommand Video Graphics Text Display"

'''
ConnectorId
IntegerArray 1 - 2
The identifier (ID) of the connector. Connector [n] has ID n. Run the following API command to find the ID: xStatus Video Input Connector.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Room Kit, Room Kit Mini
Privacy impacting No
'''

    class Input:
    
        def SetMainVideoSource():                
            """Set which input source is the main video source. You can identify the input
            source by either the physical connector that it is connected to (ConnectorId) or
            the logical source identifier (SourceId). You can combine multiple input sources
            in a single main video stream (the maximum number of different input sources
            depend on the type of video conferencing device) by adding multiple ConnectorIds
            or SourceIds in the same command. There cannot be a mix of identifier types in
            the same command; use eit..."""                
            return "xCommand Video Input SetMainVideoSource"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        class MainVideo:
        
            def Mute():                
                """Stop sending video from the device. Selfview is also turned off. This command
                does not affect the presentation channel."""                
                return "xCommand Video Input MainVideo Mute"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

            def Unmute():                
                """Start sending video from the device if previously turned off using the Video
                Input MainVideo Mute command (or, if available, the "Turn off video" button on
                the user interface). Selfview is also available."""                
                return "xCommand Video Input MainVideo Unmute"

'''
LayoutName
Required String 0 - 128
The name of the layout family.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Layout:
    
        def SetLayout():                
            """Select which video layout family to use locally. You must choose a value from
            the list returned by the Video Layout CurrentLayouts AvailableLayouts[n]
            LayoutName status."""                
            return "xCommand Video Layout SetLayout"

'''
CustomLayoutName
String 0 - 128
To use a custom layout, specify this parameter and the layout name.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class LayoutFamily:
        
            def Set():                
                """Select which video layout family to use locally. This setting applies only when
                using a device's built-in MultiSite feature (optional) to host a multipoint
                video conference."""                
                return "xCommand Video Layout LayoutFamily Set"

'''
Layout
Literal Equal, Prominent
Select the layout you wish to use for the video composition. Equal: All sources are shown in same-sized images on the output. Prominent: The first source is shown as a large image, and the next sources are shown as smaller images placed below.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Room Kit
Privacy impacting No
'''

    class Matrix:
    
        def Assign():                
            """Video Matrix commands are a smart overlay to the xCommand Video Layout commands
            to make it easy to do simple video compositions."""                
            return "xCommand Video Matrix Assign"

'''
Output
Integer 1 - 2
Choose the output you want to reset.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Codec Plus, Room 55 Dual, Room 70 Dual, Room 70 Single, Room Kit
Privacy impacting No
'''

        def Reset():                
            """Reset the content on the output to the default layout xCommand Video Matrix
            commands are a smart overlay to the xCommand Video Layout commands to make it
            easy to do simple video compositions."""                
            return "xCommand Video Matrix Reset"

'''
OutputA
Required Integer 1 - 2
The output you are swapping from.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Codec Plus, Room 55 Dual, Room 70 Dual, Room 70 Single, Room Kit
Privacy impacting No
'''

        def Swap():                
            """Swap the content defined with xCommand Video Matrix Assign between two outputs.
            xCommand Video Matrix commands are a smart overlay to the xCommand Video Layout
            commands to make it easy to do simple video compositions."""                
            return "xCommand Video Matrix Swap"

'''
Output
Required Integer 1 - 2
Choose the output you wish to remove the source from.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Room Kit
Privacy impacting No
'''

        def Unassign():                
            """Remove a source from an output. Just as with xCommand Video Matrix Assign the
            layout engine will recompose the remaining sources automatically. xCommand Video
            Matrix commands are a smart overlay to the xCommand Video Layout commands to
            make it easy to do simple video compositions."""                
            return "xCommand Video Matrix Unassign"

'''
Back-end Any
User roles Admin, User
Products Codec Plus, Codec Pro, Room 55, Room 70 Dual G2, Room 70 Single, Room 70 Single G2, Room Kit
Privacy impacting No
'''

    class Output:
    
        class HDMI:
        
            class Passthrough:
            
                def Start():                
                    """"""                
                    return "xCommand Video Output HDMI Passthrough Start"

'''
Back-end Any
User roles Admin, User
Products Codec Plus, Codec Pro, Room 55, Room 70 Dual G2, Room 70 Single, Room 70 Single G2, Room Kit
Privacy impacting No
'''

                def Stop():                
                    """"""                
                    return "xCommand Video Output HDMI Passthrough Stop"

'''
Position
Required Literal CenterLeft, CenterRight, LowerLeft, LowerRight, UpperCenter, UpperLeft, UpperRight, DockLowerLeft, DockCenterLeft
Select one of the predefined positions.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class PresentationPIP:
    
        def Set():                
            """Sets position for the presentation PiP (picture in picture)."""                
            return "xCommand Video PresentationPIP Set"

'''
View
Required Literal Default, Maximized, Minimized
Select Default when you want the presentation to be viewed with the default settings for the codec. Select Maximized when you want the presentation to be displayed in full screen. Select Minimized when you want the presentation to be displayed in a small picture on screen.
'''

'''
Back-end Any
User roles Admin, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class PresentationView:
    
        def Set():                
            """Set the presentation view mode"""                
            return "xCommand Video PresentationView Set"

'''
FullscreenMode
Literal On, Off
Choose between displaying the self-view in full screen or as picture-in-picture.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Selfview:
    
        def Set():                
            """Sets self-view on/off and specifies its size and position. If the parameter is
            not specified, current value is used."""                
            return "xCommand Video Selfview Set"

'''
Type
Literal All, Signage, WebApps Default: All
All: Deletes the session data for all web view types. Signage: Deletes the session data related to digital signage. WebApps: Deletes the session data related to all web views except digital signage.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

class WebEngine:

    def DeleteStorage():                
        """Deletes session data for web view types, such as digital signage and web apps."""                
        return "xCommand WebEngine DeleteStorage"

'''
BookingId
String 0 - 255
The BookingId is necessary for snooze and ignore to function correctly on a device. It is an identifier that an external booking system (for example, TMS or CTS-MAN) can use for its own references to match placed calls with the booking systems internal identifier for a meeting. This can be any string, for example, a GUID. The booking Id is supplied in call logs, call events etc for the call.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class WebRTC:

    def Join():                
        """Join a WebRTC meeting (for example, Microsoft Teams or Google Meet). WebRTC is
        only available for devices that are registered to an on-premises service and
        linked to Webex Edge for Devices, and for devices that are registered to the
        Webex cloud service."""                
        return "xCommand WebRTC Join"

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

    class Provider:
    
        class Current:
        
            class Diagnostics:
            
                def Send():                
                    """Sends diagnostics from the WebRTC meeting app (for example, Microsoft Teams) to
                    the meeting provider (for example, Microsoft). These diagnostics are not
                    available to Cisco. WebRTC is only available for devices that are registered to
                    an on-premises service and linked to Webex Edge for Devices, and for devices
                    that are registered to the Webex cloud service."""                
                    return "xCommand WebRTC Provider Current Diagnostics Send"

'''
MeetingNumber
Required String 0 - 255
The meeting code generated by the Google Meet meeting invitation.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting No
'''

        class GoogleMeet:
        
            class MeetingNumber:
            
                def Validate():                
                    """Validates the meeting number provided for a Google Meet meeting. WebRTC is only
                    available for devices that are registered to an on-premises service and linked
                    to Webex Edge for Devices, and for devices that are registered to the Webex
                    cloud service. Google Meet is not currently available on Desk."""                
                    return "xCommand WebRTC Provider GoogleMeet MeetingNumber Validate"

'''
DisplayName
String 0 - 255
The display name of the remote participant.
'''

'''
Back-end Any
User roles Admin, Integrator, User
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

class Webex:

    def Join():                
        """Join the Webex Meeting specified by the meeting number. Add optional
        information, such as the display name or a tag, to identify the call in the call
        history."""                
        return "xCommand Webex Join"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

    class Registration:
    
        def Cancel():                
            """Cancel device registration to Cisco Webex. This command only works in the short
            period after the registration is started with xCommand Webex Registration Start."""                
            return "xCommand Webex Registration Cancel"

'''
Confirm
Required Literal Yes
Enter Yes, case-insensitive, to confirm that you will proceed with the command. Any other text will cancel the request.
'''

'''
Back-end On-prem
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def ConvertToCloud():                
            """Convert a device to be managed by the Cisco Webex cloud service. This is only
            available on systems linked with Webex Edge for Devices. All current connections
            to on-premises services for calling and directory will be replaced with cloud
            data sources. To convert back to on-premises again, the device must factory
            reset."""                
            return "xCommand Webex Registration ConvertToCloud"

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Logout():                
            """Log a user out from a personalized system, typically Hot Desked shared system or
            personalized Webex Edge device."""                
            return "xCommand Webex Registration Logout"

'''
AccountLinkMode
Literal Asynchronous
When adding this parameter, the command returns immediately and doesn’t wait for account linking to complete. This is convenient when moving a shared mode device to personal mode; otherwise, the command may time out and return “failed” before the account linking is complete. This parameter only applies to devices that are registered to the Webex cloud or linked to Webex Edge for Devices.
'''

'''
Back-end Any
User roles Admin
Products Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
Privacy impacting ⚠️ Yes
'''

        def Start():                
            """Register a device to the Webex cloud service, or link it to Webex Edge for
            Devices, by entering the device activation code. Also choose whether to keep or
            deactivate existing local users and macros. Unless you add the AccountLinkMode
            parameter, you will get a confirmation that the registration has been successful
            or failed."""                
            return "xCommand Webex Registration Start"

