# coding=utf-8
# *** WARNING: this file was generated by crd2pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

SNAKE_TO_CAMEL_CASE_TABLE = {
    "access_key_id": "accessKeyID",
    "access_token_secret_ref": "accessTokenSecretRef",
    "account_secret_ref": "accountSecretRef",
    "acme_dns": "acmeDNS",
    "api_key_secret_ref": "apiKeySecretRef",
    "api_token_secret_ref": "apiTokenSecretRef",
    "api_version": "apiVersion",
    "app_role": "appRole",
    "azure_dns": "azureDNS",
    "ca_bundle": "caBundle",
    "class_": "class",
    "client_id": "clientID",
    "client_secret_secret_ref": "clientSecretSecretRef",
    "client_token_secret_ref": "clientTokenSecretRef",
    "cloud_dns": "cloudDNS",
    "cname_strategy": "cnameStrategy",
    "credentials_ref": "credentialsRef",
    "crl_distribution_points": "crlDistributionPoints",
    "disable_account_key_generation": "disableAccountKeyGeneration",
    "dns_names": "dnsNames",
    "dns_zones": "dnsZones",
    "enable_duration_feature": "enableDurationFeature",
    "external_account_binding": "externalAccountBinding",
    "group_name": "groupName",
    "hosted_zone_id": "hostedZoneID",
    "hosted_zone_name": "hostedZoneName",
    "ingress_template": "ingressTemplate",
    "key_algorithm": "keyAlgorithm",
    "key_id": "keyID",
    "key_secret_ref": "keySecretRef",
    "label_selector": "labelSelector",
    "last_registered_email": "lastRegisteredEmail",
    "last_transition_time": "lastTransitionTime",
    "match_expressions": "matchExpressions",
    "match_fields": "matchFields",
    "match_labels": "matchLabels",
    "mount_path": "mountPath",
    "node_affinity": "nodeAffinity",
    "node_selector": "nodeSelector",
    "node_selector_terms": "nodeSelectorTerms",
    "observed_generation": "observedGeneration",
    "ocsp_servers": "ocspServers",
    "pod_affinity": "podAffinity",
    "pod_affinity_term": "podAffinityTerm",
    "pod_anti_affinity": "podAntiAffinity",
    "pod_template": "podTemplate",
    "preferred_chain": "preferredChain",
    "preferred_during_scheduling_ignored_during_execution": "preferredDuringSchedulingIgnoredDuringExecution",
    "priority_class_name": "priorityClassName",
    "private_key_secret_ref": "privateKeySecretRef",
    "required_during_scheduling_ignored_during_execution": "requiredDuringSchedulingIgnoredDuringExecution",
    "resource_group_name": "resourceGroupName",
    "role_id": "roleId",
    "secret_access_key_secret_ref": "secretAccessKeySecretRef",
    "secret_name": "secretName",
    "secret_ref": "secretRef",
    "self_signed": "selfSigned",
    "service_account_name": "serviceAccountName",
    "service_account_secret_ref": "serviceAccountSecretRef",
    "service_consumer_domain": "serviceConsumerDomain",
    "service_type": "serviceType",
    "skip_tls_verify": "skipTLSVerify",
    "solver_name": "solverName",
    "subscription_id": "subscriptionID",
    "tenant_id": "tenantID",
    "token_secret_ref": "tokenSecretRef",
    "toleration_seconds": "tolerationSeconds",
    "topology_key": "topologyKey",
    "tsig_algorithm": "tsigAlgorithm",
    "tsig_key_name": "tsigKeyName",
    "tsig_secret_secret_ref": "tsigSecretSecretRef",
}

CAMEL_TO_SNAKE_CASE_TABLE = {
    "accessKeyID": "access_key_id",
    "accessTokenSecretRef": "access_token_secret_ref",
    "accountSecretRef": "account_secret_ref",
    "acmeDNS": "acme_dns",
    "apiKeySecretRef": "api_key_secret_ref",
    "apiTokenSecretRef": "api_token_secret_ref",
    "apiVersion": "api_version",
    "appRole": "app_role",
    "azureDNS": "azure_dns",
    "caBundle": "ca_bundle",
    "class": "class_",
    "clientID": "client_id",
    "clientSecretSecretRef": "client_secret_secret_ref",
    "clientTokenSecretRef": "client_token_secret_ref",
    "cloudDNS": "cloud_dns",
    "cnameStrategy": "cname_strategy",
    "credentialsRef": "credentials_ref",
    "crlDistributionPoints": "crl_distribution_points",
    "disableAccountKeyGeneration": "disable_account_key_generation",
    "dnsNames": "dns_names",
    "dnsZones": "dns_zones",
    "enableDurationFeature": "enable_duration_feature",
    "externalAccountBinding": "external_account_binding",
    "groupName": "group_name",
    "hostedZoneID": "hosted_zone_id",
    "hostedZoneName": "hosted_zone_name",
    "ingressTemplate": "ingress_template",
    "keyAlgorithm": "key_algorithm",
    "keyID": "key_id",
    "keySecretRef": "key_secret_ref",
    "labelSelector": "label_selector",
    "lastRegisteredEmail": "last_registered_email",
    "lastTransitionTime": "last_transition_time",
    "matchExpressions": "match_expressions",
    "matchFields": "match_fields",
    "matchLabels": "match_labels",
    "mountPath": "mount_path",
    "nodeAffinity": "node_affinity",
    "nodeSelector": "node_selector",
    "nodeSelectorTerms": "node_selector_terms",
    "observedGeneration": "observed_generation",
    "ocspServers": "ocsp_servers",
    "podAffinity": "pod_affinity",
    "podAffinityTerm": "pod_affinity_term",
    "podAntiAffinity": "pod_anti_affinity",
    "podTemplate": "pod_template",
    "preferredChain": "preferred_chain",
    "preferredDuringSchedulingIgnoredDuringExecution": "preferred_during_scheduling_ignored_during_execution",
    "priorityClassName": "priority_class_name",
    "privateKeySecretRef": "private_key_secret_ref",
    "requiredDuringSchedulingIgnoredDuringExecution": "required_during_scheduling_ignored_during_execution",
    "resourceGroupName": "resource_group_name",
    "roleId": "role_id",
    "secretAccessKeySecretRef": "secret_access_key_secret_ref",
    "secretName": "secret_name",
    "secretRef": "secret_ref",
    "selfSigned": "self_signed",
    "serviceAccountName": "service_account_name",
    "serviceAccountSecretRef": "service_account_secret_ref",
    "serviceConsumerDomain": "service_consumer_domain",
    "serviceType": "service_type",
    "skipTLSVerify": "skip_tls_verify",
    "solverName": "solver_name",
    "subscriptionID": "subscription_id",
    "tenantID": "tenant_id",
    "tokenSecretRef": "token_secret_ref",
    "tolerationSeconds": "toleration_seconds",
    "topologyKey": "topology_key",
    "tsigAlgorithm": "tsig_algorithm",
    "tsigKeyName": "tsig_key_name",
    "tsigSecretSecretRef": "tsig_secret_secret_ref",
}
