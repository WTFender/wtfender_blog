## Steps
#### 1. Add a webhook to your Slack team.

#### 2. Create your AIE alarm with fields that you want to pass to your webhook.

#### 3. Create a powershell script accepting the fields as parameters:

<script src="https://gist.github.com/WTFender/aad9eee612dab9a012a256be93da54bc.js?file=basic.ps1"></script>

#### 4. Create the actions.xml manifest with the same parameters/fields:

<script src="https://gist.github.com/WTFender/aad9eee612dab9a012a256be93da54bc.js?file=actions.xml"></script>

#### 5. Create your SmartResponse Plugin using the powershell script and manifest.

#### 6. Set your SmartResponse as an action to your AIE alarm, mapping the correct parameters:

<img src="/static/img/lr_webhooks2.png">

#### 7. Trigger your alarm and observe the webhook:

<img src="/static/img/lr_webhooks3.png">

## Better Alarm Examples

#### [Privileged User Group Changes](https://github.com/WTFender/logrhythm-slack-webhooks/blob/master/better%20examples/privileged-user-group-change/privileged-user-group-change.ps1)
<img src="/static/img/lr_webhooks4.png">

#### [Authentication Failures](https://github.com/WTFender/logrhythm-slack-webhooks/blob/master/better%20examples/auth-failure/auth-failure.ps1)
<img src="/static/img/lr_webhooks5.png">

#### [Suspicious IP Inbound](https://github.com/WTFender/logrhythm-slack-webhooks/blob/master/better%20examples/suspicious-ip-inbound/suspicious-ip-inbound.ps1)
<img src="/static/img/lr_webhooks6.png">

#### [Suspicious IP Outbound](https://github.com/WTFender/logrhythm-slack-webhooks/blob/master/better%20examples/suspicious-ip-outbound/suspicious-ip-outbound.ps1)
<img src="/static/img/lr_webhooks7.png">

### Credit

[jgigler/Powershell.Slack](https://github.com/jgigler/Powershell.Slack)