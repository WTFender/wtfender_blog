Here is a LogRhythm regex parser that I use for F5 WAF syslog violations.

<script src="https://gist.github.com/WTFender/a857dc47ca2b367e27061ba6a19390b5.js?file=f5_parser.regex"></script>

This is for the actual WAF violations, not the L7 DDoS logs. Some of the tags are LogRhythm specific, but this can be easily modified for whatever SIEM you’d like.

The LogRhythm field tags that I use are mapped like this:

<script src="https://gist.github.com/WTFender/a857dc47ca2b367e27061ba6a19390b5.js?file=tags.regex"></script>

Moving on to sub-rules, I’ve created common events with similar naming schemes to the different violation types (Illegal Method, Illegal File Type, etc). Using the `<subject>` tag, I map each log to a relevant common event. However, some logs have multiple violation types, separated by a comma. I group all of these into a common event named “Multiple Violations.”

Here is an example of sub-rules creating common events:

<script src="https://gist.github.com/WTFender/a857dc47ca2b367e27061ba6a19390b5.js?file=subject.regex"></script>

Lastly, the `<vmid>` tag holds the response code for the request, if the request was allowed it will be a typical HTTP response code (200, 404, etc) and if it was blocked it will be 0. I use the `<vmid>` to set the classification of the common event (in my case; security attack and failed security attack). I simply identify blocked and permitted requests using the following:

<script src="https://gist.github.com/WTFender/a857dc47ca2b367e27061ba6a19390b5.js?file=vmid.regex"></script>

Keep in mind that the actual source IP for the logs is being tracked as `<snatip>`, not `<sip>`. Build your dashboards accordingly.

Here is the violation log format and example log, provided in the F5 support article:

<script src="https://gist.github.com/WTFender/a857dc47ca2b367e27061ba6a19390b5.js?file=sample.regex"></script>