# cfn-mp-ql-rules
Python Package (CFN Lint Rules)

## List of rules

The following custom CFN Lint rules are provided by this repository. Rule IDs and descriptions come from the metadata exposed by each implementation class.

| Rule ID | Implementation | Description |
|---|---|---|
| `E-IAM-IGNORE-JUSTIFICATION` | [`IAMExcludeReason`](cfn_mp_ql_rules/IAMExcludeReason.py) | excluding IAM best practices requires justification |
| `E9007` | [`IAMPartition`](cfn_mp_ql_rules/IAMPartition.py) | ARNs should be partition argnostic |
| `E9008` | [`Base`](cfn_mp_ql_rules/QSID.py) | QSIDs should be in template description |
| `E9101` | [`Base`](cfn_mp_ql_rules/InclusiveLanguage.py) | Use welcoming and inclusive language |
| `E9903` | [`MissingParameter`](cfn_mp_ql_rules/stack/MissingParameter.py) | Parameters missing for nested stack |
| `E9904` | [`ParameterNotInChild`](cfn_mp_ql_rules/stack/ParameterNotInChild.py) | Parameters in passed to stack resource but not defined in child |
| `EAppStreamPlaintextCreds` | [`AppStreamPlaintextCreds`](cfn_mp_ql_rules/AppStreamPlaintextCreds.py) | No plaintext password or ref to a default value on AppStream DirectoryConfig Credentials |
| `EBSVolumeEncryption` | [`EBSVolumeEncryption`](cfn_mp_ql_rules/EBSVolumeEncryption.py) | EBS volume missing enryption |
| `ECognitoUserPoolMfaConfiguration` | [`CFNNAGF78`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::Cognito::UserPool should have MfaConfiguration enabled |
| `EEFSFilesystemEncrypted` | [`CFNNAGF32`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::EFS::Filesystem should have Encrypted enabled |
| `EElastiCacheReplicationGroupAtRestEncryptionEnabled` | [`CFNNAGF25`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::ElastiCache::ReplicationGroup should have AtRestEncryptionEnabled enabled |
| `EIAMAccountIDInPrincipal` | [`IAMResourceWildcard`](cfn_mp_ql_rules/IAMNoAccountNumber.py) | Hard-coded account IDs are unacceptable. |
| `EIAMNoInlinePolicy` | [`IAMNoInlinePolicy`](cfn_mp_ql_rules/IAMNoInlinePolicy.py) | No inline IAM policies for a user |
| `EIAMPolicyActionNotAction` | [`IAMResourceWildcard`](cfn_mp_ql_rules/IAMNotAction.py) | Combining Action and NotAction is a bad idea. |
| `EIAMPolicyActionNotResource` | [`IAMResourceWildcard`](cfn_mp_ql_rules/IAMNotResource.py) | Combining Action and NotAction is a bad idea. |
| `EIAMPolicyActionWildcard` | [`IAMActionWildcard`](cfn_mp_ql_rules/IAMActionWildcard.py) | * on Action property is a bad idea |
| `EIAMPolicyOnlyGroup` | [`IAMPolicyOnlyGroup`](cfn_mp_ql_rules/IAMPolicyOnlyGroup.py) | No direct user on IAM policy |
| `EIAMPolicyWildcardResource` | [`IAMResourceWildcard`](cfn_mp_ql_rules/IAMResourceWildcard.py) | * on Resource property is a bad idea |
| `EIAMUserNotInGroup` | [`IAMPolicyOnlyGroup`](cfn_mp_ql_rules/IAMUserNotInGroup.py) | User not assigned to group |
| `EKMSKeyEnableKeyRotation` | [`CFNNAGF103`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::KMS::Key should have EnableKeyRotation enabled |
| `EMQBrokerPassword` | [`MQBrokerPassword`](cfn_mp_ql_rules/MQBrokerPassword.py) | No plaintext password or ref to a default value on a AmazonMQ Broker User |
| `ENeptuneDBClusterStorageEncrypted` | [`CFNNAGF33`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::Neptune::DBCluster should have StorageEncrypted enabled |
| `ENetworkACLRepeatRules` | [`NetworkACLRepeatRules`](cfn_mp_ql_rules/NetworkACLRepeatRules.py) | No repeat rules on Network ACL unless different types |
| `EPolicyWildcardPrincipal` | [`IAMPrincipalWildcard`](cfn_mp_ql_rules/PrincipalWildcard.py) | * on Principal property is a bad idea |
| `ERDSDBInstancePubliclyAccessible` | [`CFNNAGF22`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::RDS::DBInstance should have PubliclyAccessible enabled |
| `ERDSStorageEncryptionEnabled` | [`StorageEncryptionEnabled`](cfn_mp_ql_rules/StorageEncryptionEnabled.py) | AWS::RDS::DBCluster should have StorageEncryption enabled |
| `ERedshiftClusterEncrypted` | [`CFNNAGF28`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::Redshift::Cluster should have Encrypted enabled |
| `ES3NoPublicReadWrite` | [`S3NoPublicReadWrite`](cfn_mp_ql_rules/S3NoPublicReadWrite.py) | No public read-write ACL on S3 |
| `ESimpleDBDomainProhibited` | [`NoSimpleDBDomain`](cfn_mp_ql_rules/ProhibitedResources.py) | AWS::SimpleDB::Domain is prohibited |
| `EValidateIAMRuleExclusions` | [`ValidateRuleExclusions`](cfn_mp_ql_rules/ValidateIAMExclusions.py) | * on Resource property is a bad idea |
| `EWAFv2WebACLProhibited` | [`WAFV2NoDefaultAllow`](cfn_mp_ql_rules/ProhibitedResourceProperties.py) | AWS::WAFv2::WebACL should not have DefaultAction.Allow enabled |
| `EWorkspacesWorkspaceRootVolumeEncryptionEnabled` | [`CFNNAGF29p1`](cfn_mp_ql_rules/RequiredResourceProperties.py) | AWS::Workspaces::Workspace should have RootVolumeEncryptionEnabled enabled |
| `W9001` | [`Base`](cfn_mp_ql_rules/Casing.py) | Name casing should be PascalCase |
| `W9002` | [`Base`](cfn_mp_ql_rules/Labels.py) | Each parameter should have a label |
| `W9003` | [`Base`](cfn_mp_ql_rules/Groups.py) | Each parameter should be in a group |
| `W9004` | [`Base`](cfn_mp_ql_rules/Descriptions.py) | Each parameter should have a description |
| `W9006` | [`Base`](cfn_mp_ql_rules/SentenceCase.py) | Parameter descriptions should be sentence case |
| `W9901` | [`DefaultParameter`](cfn_mp_ql_rules/stack/DefaultParameter.py) | Parameters missing for nested stack |
