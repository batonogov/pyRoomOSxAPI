class Audio:
    def __init__(self) -> str:
        pass

    def Diagnostics(MeasurementLength=6, Output='HDMI', Volume=20):
        '''
            This command measures the audio delay/latency in a device that is connected to the video conferencing device. A typical use case it to measure the delay in a TV connected to the video conferencing device via the HDMI connector. If the delay in a TV is too high, the real-time experience of a video call will be substantially degraded. If the delay is more than 50 ms we recommend the user to find a TV setting that has shorter delay. Typical TV settings that can reduce the delay are: Gaming Mode and...
            
            ### MeasurementLength:
            Integer 1 - 100 Default: 6
            The length of the measurement in number of seconds. In a noisy environment a longer measurement duration will give a more reliable and robust result.
            
            ### Output:
            Literal HDMI, Line, Internal, Headset, All Default: HDMI
            All: Measure the maximum delay of all outputs. HDMI: Measure the delay of the device connected to the HDMI output. Headset: Measure the delay of the headset (only available on video conferencing devices that have a headset). Internal: Measure the delay of the internal loudspeaker (only available on video conferencing devices that have an internal loudspeaker). Line: Measure the delay of the device connected to the Line output (only available on video conferencing devices that have a Line output).
            
            ### Volume:
            Integer 0 - 50 Default: 20
            The volume of the test signal. In a noisy environment a higher volume gives more reliable and robust results.

            ---
            
            ```
            Back-end: Any
            User roles: Admin, User
            Products: Room Series
            Privacy impacting: No
            ```
        '''

        return f'xCommand Audio Diagnostics MeasureDelay MeasurementLength: {MeasurementLength}, Output: {Output}, Volume: {Volume}'

    def Diagnostics_Advanced(Channel=0, MeasurementLength=3, Output='All', Volume=20):
        '''
            This command sends out a noise signal sequentially on all audio output connectors and measures the room impulse response (RIR) between the output and the microphones. If a RIR is detected, the detected number of microphones (input), the detected number of output connectors, and the detected delay between the output and input is reported back. Example: xCommand Audio Diagnostics Advanced Run Volume: 50 MeasurementLength: 1 Result returned -> OK *r AdvancedRunResult (status=OK): *r AdvancedRunResu...

            ### Channel
            Integer 0 - 13 Default: 0
            The channel number, from left to right, of the selected output.

            ### MeasurementLength
            Integer 1 - 100 Default: 3
            The length of the measurement in number of seconds. In a noisy environment a longer measurement duration will give a more reliable and robust result.
            
            ### Output
            Literal HDMI, Line, Internal, Headset, All Default: All
            The output where the test signal should be directed. All: Measure the RIR on all outputs. HDMI: Measure the room impulse response (RIR) of the device connected to the HDMI output. Headset: Measure the RIR of the headset (only available on video conferencing devices that have a headset). Internal: Measure the RIR of the internal loudspeaker (only available on video conferencing devices that have an internal loudspeaker). Line: Measure the RIR of the device connected to the Line output (only available on video conferencing devices that have a Line output).
            
            ### Volume
            Integer 0 - 50 Default: 20
            The volume of the test signal. In a noisy environment a higher volume gives more reliable and robust results.
            
            ---

            ```
            Back-end: Any
            User roles: Admin, User
            Products: Room Series
            Privacy impacting: No
            ```
        '''

        return f'xCommand Audio Diagnostics Advanced Run Channel: {Channel}, MeasurementLength: {MeasurementLength}, Output: {Output}, Volume: {Volume}'

    class Diagnostics_AecReverb():
        def Reset():
            '''
                Reset the acoustic echo cancellation. This command is useful when making changes in the acoustical treatment of the room. All previous adaptations are cleared and a new measurement of the reverberation time is made. This is not allowed during a call.
            
                ---

                ```
                Back-end: Any
                User roles: Admin, User
                Products: Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
                Privacy impacting: No
                ```
            '''
            
            return f'xCommand Audio Diagnostics AecReverb Reset'

        def Run():
            '''
                The command uses the acoustic echo canceller to give an estimate of the reverberation time in the room. This is done transparently, without interruption of the normal operation of the endpoint.
            
                ---

                ```
                Back-end: Any
                User roles: Admin, User
                Products: Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
                Privacy impacting: No
                ```
            '''

            return f'xCommand Audio Diagnostics AecReverb Run'

    class Microphones():
        def Mute():
            '''
                Mute all microphones.

                ---

                ```
                Back-end: Any
                User roles: Admin, Integrator, User
                Products: Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
                Privacy impacting: ⚠️ Yes
                ```
            '''

            return f'xCommand Audio Microphones Mute'

        def ToggleMute():
            '''
                Toggle the microphone between muted and unmuted.

                ---

                ```
                No parameters
                Back-end: Any
                User roles: Admin, Integrator, User
                Products: Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
                Privacy impacting: ⚠️ Yes
                ```
            '''
            
            return f'xCommand Audio Microphones ToggleMute'

        def Unmute():
            '''
                Unmute all microphones.

                ---

                ```
                No parameters
                Back-end	Any
                User roles	Admin, Integrator, User
                Products	Board Series, Desk, Desk Hub, Desk Limited, Desk Mini, Desk Pro, Room Series
                Privacy impacting	⚠️ Yes
                ```
            '''
            
            return f'xCommand Audio Microphones Unmute'


    def Microphones_MusicMode(action=None):
        '''
            ## Actions:

            ### Start

            Start using MusicMode in the current call. Music mode allows the dynamic range of music go through. When Music mode is in use, sound level variations are transmitted intact and the noise filtering is kept to a minimum. MusicMode is automatically turned off when the call ends.

            ### Stop

            Stop using MusicMode in the current call.
        '''

        if action:
            return f'{__name__.split(".")[-1]} {Audio.__name__} Microphones MusicMode {action}'

    def Microphones_NoiseRemoval(action=None):
        '''
        ## Actions:

        ### Activate

        Activate noise removal on the device. For this to take effect, you need to enable xConfiguration Audio Microphones NoiseRemoval Mode to enable the noise removal feature on the device.

        ### Deactivate

        Deactivate noise removal on the device.
        '''

        if action:
            return f'{__name__.split(".")[-1]} {Audio.__name__} Microphones NoiseRemoval {action}'

    # def Sound():
    #     '''
    #         Play a specified audio sound.
    #     '''
    #     pass

    class Sound():
        def Play():
            return 1

    def SoundsAndAlerts_Ringtone():
        pass

    def Volume(action='None'):
        return f'{__name__.split(".")[-1]} {Audio.__name__} {Audio.Volume.__name__} {action}'

    def VuMeter():
        pass

class Bookings:
    def __init__(self) -> str:
        pass

class Call:
    def __init__(self) -> str:
        pass

class Video:
    def __init__(self) -> str:
        pass

    def ActiveSpeakerPIP():
        pass

    def CEC_Input():
        pass

    def CEC_Output():
        pass

    def Graphics():
        pass

    def Graphics_Text():
        pass

    def Input():
        pass

    def Input_MainVideo():
        pass

    def Layout():
        pass

    def Layout_LayoutFamily():
        pass

    def Matrix():
        pass

    def PresentationPIP():
        pass

    def PresentationView():
        pass

    def Selfview():
        pass
