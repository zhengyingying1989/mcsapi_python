import sys
from mosclient.common import utils


@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeInstanceTypes(client, args):
    """ List all instance types """
    val = client.DescribeInstanceTypes(args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'InstanceType')


def do_DescribeTemplates(client, args):
    """ List all image templates """
    val = client.DescribeTemplates()
    utils.print_list(val, 'Template')


def do_GetBalance(client, args):
    """ Get balance """
    val = client.GetBalance()
    utils.print_dict(val)


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--duration', metavar='<DURATION>', help='Renew instance duration, in H or M, eg 72H, 1M')
def do_RenewInstance(client, args):
    """ Renew an instance """
    client.RenewInstance(args.id, duration=args.duration)


@utils.arg('id', metavar='<ID>', help='ID of instance')
def do_GetInstanceContractInfo(client, args):
    """ Query instance contract information """
    val = client.GetInstanceContractInfo(args.id)
    utils.print_dict(val)


@utils.arg('image', metavar='<IMAGE>', help='ID of image')
@utils.arg('instance_type', metavar='<INSTANCE_TYPE>', help='Instance type')
@utils.arg('--duration', metavar='<DURATION>', help='Reserved instance duration, in H or M, e.g. 72H, 1M')
@utils.arg('--name', metavar='<NAME>', help='Optional instance name')
@utils.arg('--keypair', metavar='<KEYPAIR>', help='SSH key pair name')
@utils.arg('--secgroup', metavar='<SECGROUP>', help='Security group ID')
@utils.arg('--datadisk', metavar='<DISKSIZE>', type=int, help='Extra disksize in GB')
@utils.arg('--bandwidth', metavar='<BANDWIDTH>', type=int, help='Extra external bandwidth in Mbps')
def do_CreateInstance(client, args):
    """ Create servers """
    val = client.CreateInstance(args.image, args.instance_type,
                                duration=args.duration,
                                name=args.name,
                                keypair=args.keypair,
                                secgroup=args.secgroup,
                                datadisk=args.datadisk,
                                bandwidth=args.bandwidth)
    utils.print_dict(val)


@utils.arg('id', metavar='<ID>', help='ID of instance')
def do_DescribeInstanceStatus(client, args):
    """ Get status of an instance """
    val = client.DescribeInstanceStatus(args.id)
    utils.print_dict(val)


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--key-file', metavar='<PRIVATE_KEY>', help='Private key to decrypt password')
def do_GetPasswordData(client, args):
    """ Get initial password of an instance """
    val = client.GetPasswordData(args.id, key_file=args.key_file)
    utils.print_dict(val)


@utils.arg('--id', metavar='<ID>', action='append', help='ID of instance')
@utils.arg('--name', metavar='<NAME>', action='append', help='Name of instance')
@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeInstances(client, args):
    """ Get details of all or specified instances """
    val = client.DescribeInstances(args.id, args.name, args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'Instance')


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeInstanceVolumes(client, args):
    """ List all disks of an instance """
    val = client.DescribeInstanceVolumes(args.id, args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'InstanceVolume')


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeInstanceNetworkInterfaces(client, args):
    """ List all network interfaces of an instance """
    val = client.DescribeInstanceNetworkInterfaces(args.id, args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'InstanceNetworkInterface')


@utils.arg('id', metavar='<ID>', help='ID of instance')
def do_StartInstance(client, args):
    """ Start an instance """
    client.StartInstance(args.id)


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--force', action='store_true', help='Force stop running isntance')
def do_StopInstance(client, args):
    """ Stop an instance """
    client.StopInstance(args.id, force=args.force)


@utils.arg('id', metavar='<ID>', help='ID of instance')
def do_RebootInstance(client, args):
    """ Reboot an instance """
    client.RebootInstance(args.id)


@utils.arg('id', metavar='<ID>', help='ID of instance')
def do_TerminateInstance(client, args):
    """ Terminate an instance """
    client.TerminateInstance(args.id)


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--image', metavar='<IMAGE>', help='ID of root image template')
def do_RebuildInstanceRootImage(client, args):
    """ Rebuild root image of an instance """
    client.RebuildInstanceRootImage(args.id, image_id=args.image)


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('instance_type', metavar='<INSTANCE_TYPE>', help='Instance type')
@utils.arg('--duration', metavar='<DURATION>', help='Reserved instance duration, in H or M, e.g. 72H, 1M')
@utils.arg('--datadisk', metavar='<DISKSIZE>', required=True, type=int, help='Extra disksize in GB')
@utils.arg('--bandwidth', metavar='<BANDWIDTH>', required=True, type=int, help='Extra external bandwidth in Mbps')
def do_ChangeInstanceType(client, args):
    """ Change instance type """
    client.ChangeInstanceType(args.id, args.instance_type, duration=args.duration,
                              datadisk=args.datadisk, bandwidth=args.bandwidth)


@utils.arg('id', metavar='<ID>', help='ID of instance')
def do_GetInstanceMetadata(client, args):
    """ Get metadata of an instance """
    val = client.GetInstanceMetadata(args.id)
    utils.print_dict(val)


@utils.arg('id', metavar='<ID>', help='ID of instance')
@utils.arg('--data', metavar='<KEY:VALUE>', action='append', help='Key and value pair, separated by coma:')
def do_PutInstanceMetadata(client, args):
    """ Put metadata of an instance """
    data = {}
    if args.data:
        for d in args.data:
            if d.find(':') > 0:
                k = d[:d.find(':')]
                v = d[(d.find(':')+1):]
            else:
                k = d
                v = ''
            data[k] = v
    if len(data) == 0:
        raise Exception('No data to put')
    client.PutInstanceMetadata(args.id, data)


@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeKeyPairs(client, args):
    """ List all keypairs """
    val = client.DescribeKeyPairs(args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'KeyPair')


@utils.arg('name', metavar='<NAME>', type=str, help='Name of keypair')
@utils.arg('--key-file', metavar='<PUBLIC_KEY_FILE>', type=str, help='Public key file path')
def do_ImportKeyPair(client, args):
    """ Import SSH keypairs """
    if args.key_file is not None:
        with open(args.key_file) as pf:
            pubkey = pf.read()
    else:
        pubkey = sys.stdin.read()
    if pubkey is not None and len(pubkey) > 0:
        val = client.ImportKeyPair(args.name, pubkey)
        utils.print_dict(val)
    else:
        raise Exception('No public key provided')


@utils.arg('id', metavar='<ID>', type=str, help='ID of keypair')
def do_DeleteKeyPair(client, args):
    """ Delete a keypair """
    client.DeleteKeyPair(args.id)


@utils.arg('--iid', metavar='<INSTANCE_ID>', help='ID of instance')
def do_DescribeInstanceMetrics(client, args):
    """List monitor metrics"""
    val = client.DescribeInstanceMetrics(args.iid)
    utils.print_list(val, 'Metric')


@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
def do_DescribeAlarmHistory(client, args):
    """List monitor alarm history"""
    val = client.DescribeAlarmHistory(args.limit, args.offset)
    utils.print_list(val, 'AlarmHistory')


@utils.arg('--iid', metavar='<INSTANCE_ID>', required=True, help='Instance ID')
@utils.arg('--metric', metavar='<METRIC>', required=True, help='Metric Name')
@utils.arg('--threshold', metavar='<THRESHOLD>', required=True, help='Threshold')
@utils.arg('--operator', metavar='<OPERATOR>', choices=['GT', 'EQ', 'LT'], required=True, help='Operator')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Monitor description')
def do_CreateMetricAlarm(client, args):
    """Create metric check monitor"""
    val = client.CreateMetricAlarm(args.iid, args.metric, args.operator, args.threshold, args.description)
    utils.print_dict(val)


def do_DescribeMetricAlarms(client, args):
    """List metric check"""
    val = client.DescribeMetricAlarms()
    utils.print_list(val, 'MetricAlarm')


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_DeleteMetricAlarm(client, args):
    """Delete metric check"""
    val = client.DeleteMetricAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_EnableMetricAlarm(client, args):
    """Enable a metric check"""
    val = client.EnableMetricAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_DisableMetricAlarm(client, args):
    """Disable a metric check"""
    val = client.DisableMetricAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('--iid', metavar='<INSTANCE_ID>', required=True, help='Instance ID')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Monitor description')
def do_CreateAliveAlarm(client, args):
    """Create alive check"""
    val = client.CreateAliveAlarm(args.iid, args.description)
    utils.print_dict(val)


def do_DescribeAliveAlarms(client, args):
    """List alive check"""
    val = client.DescribeAliveAlarms()
    utils.print_list(val, 'AliveAlarm')


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_DeleteAliveAlarm(client, args):
    """Delete alive check"""
    val = client.DeleteAliveAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_EnableAliveAlarm(client, args):
    """Enable a alive check"""
    val = client.EnableAliveAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_DisableAliveAlarm(client, args):
    """Disable a alive check"""
    val = client.DisableAliveAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('--iid', metavar='<INSTANCE_ID>', required=True, help='Instance ID')
@utils.arg('--tcp-port', metavar='<PORT>', required=True, help='TCP port')
@utils.arg('--description', metavar='<DESCRIPTION>', help='Monitor description')
def do_CreateTCPAlarm(client, args):
    """Create tcp check"""
    val = client.CreateTCPAlarm(args.iid, args.tcp_port, args.description)
    utils.print_dict(val)


def do_DescribeTCPAlarms(client, args):
    """List tcp check"""
    val = client.DescribeTCPAlarms()
    utils.print_list(val, 'TCPAlarm')


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_DeleteTCPAlarm(client, args):
    """Delete tcp check"""
    val = client.DeleteTCPAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_EnableTCPAlarm(client, args):
    """Enable a tcp check"""
    val = client.EnableTCPAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('mid', metavar='<MONITOR_ID>', help='ID of monitor')
def do_DisableTCPAlarm(client, args):
    """Disable a tcp check"""
    val = client.DisableTCPAlarm(args.mid)
    utils.print_dict(val)


@utils.arg('id', metavar='<INSTANCE_ID>', help='ID of tempalte')
@utils.arg('name', metavar='<TEMPLATE_NAME>', help='Name of template')
@utils.arg('--notes', metavar='<NOTES>', help='Template Notes')
def do_CreateTemplate(client, args):
    """Save root disk to new image and upload to glance."""
    val = client.CreateTemplate(args.id, args.name, notes=args.notes)
    utils.print_dict(val)

@utils.arg('id', metavar='<TEMPLATE_ID>', help='ID of template')
def do_DeleteTemplate(client, args):
    """ Delete a template """
    client.DeleteTemplate(args.id)

@utils.arg('name', metavar='<GROUP_NAME>', help='Name of security group')
@utils.arg('description', metavar='<DESCRIPTION>', help='Description of security group')
def do_CreateSecurityGroup(client, args):
    """ Create a security group """
    val = client.CreateSecurityGroup(args.name, args.description)
    utils.print_dict(val)


@utils.arg('--id', metavar='<ID>', action='append', help='ID of security group')
@utils.arg('--name', metavar='<NAME>', action='append', help='Name of security group')
@utils.arg('--limit', metavar='<NUMBER>', default=20, help='Page limit')
@utils.arg('--offset', metavar='<OFFSET>', help='Page offset')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeSecurityGroups(client, args):
    """ List all security groups """
    p = utils.convert_filter(args.filter)
    val = client.DescribeSecurityGroups(args.id, args.name, args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'SecurityGroup')


@utils.arg('id', metavar='<GROUP_ID>', help='ID of security group')
def do_DeleteSecurityGroup(client, args):
    """ Delete a security group """
    client.DeleteSecurityGroup(args.id)


@utils.arg('id', metavar='<ID>', help='ID of security group')
@utils.arg('--rule', metavar='<RULE>', action='append', help='Security rule to authorize')
def do_AuthorizeSecurityGroupIngress(client, args):
    """ Authorize an ingress rule to a security group """
    client.AuthorizeSecurityGroupIngress(args.id, args.rule)


@utils.arg('id', metavar='<ID>', help='ID of security group')
@utils.arg('--rule', metavar='<RULE>', action='append', help='Security rule to revoke')
def do_RevokeSecurityGroupIngress(client, args):
    """ Revoke an ingress rule from a security group """
    client.RevokeSecurityGroupIngress(args.id, args.rule)


@utils.arg('iid', metavar='<INSTANCE_ID>', help='ID of instance')
@utils.arg('gid', metavar='<GROUP_ID>', help='ID of security group')
def do_InstanceAssignSecurityGroup(client, args):
    """ Assign a security group to an instance """
    client.InstanceAssignSecurityGroup(args.iid, args.gid)


@utils.arg('iid', metavar='<INSTANCE_ID>', help='ID of instance')
def do_InstanceRevokeSecurityGroup(client, args):
    """ Revoke a security group from an instance """
    client.InstanceRevokeSecurityGroup(args.iid)


@utils.arg('--id', metavar='<ID>', action='append', help='ID of redis')
@utils.arg('--name', metavar='<NAME>', action='append', help='Name of redis')
@utils.arg('--limit', metavar='<LIMIT>', type=int, help='Limit')
@utils.arg('--offset', metavar='<OFFSET>', type=int, help='Limit')
@utils.arg('--filter', metavar='<FILTER>', action='append', help='Filter')
def do_DescribeRedis(client, args):
    """ Get details of all or specified redis """
    val = client.DescribeRedis(args.id, args.name, args.limit, args.offset, utils.convert_filter(args.filter))
    utils.print_list(val, 'Redis')


@utils.arg('--mem', metavar='<MEMORY>', required=True, type=int, help='Redis memory size(GB)')
@utils.arg('--duration', metavar='<DURATION>', help='Reserved redis duration, in H or M, e.g. 72H, 1M')
@utils.arg('--name', metavar='<NAME>', help='Optional redis name')
@utils.arg('--zone', metavar='<ZONE>', help='Zone')
def do_CreateRedis(client, args):
    """ Create redis """
    val = client.CreateRedis(args.mem,
                            duration=args.duration,
                            name=args.name,
                            zone=args.zone)

    utils.print_dict(val)


@utils.arg('id', metavar='<ID>', help='ID of redis')
def do_TerminateRedis(client, args):
    """ Terminate a Redis"""
    client.TerminateRedis(args.id)


@utils.arg('id', metavar='<ID>', help='ID of Redis')
@utils.arg('--duration', metavar='<DURATION>', help='Renew redis duration, in H or M, eg 72H, 1M')
def do_RenewRedis(client, args):
    """ Renew a Redis """
    client.RenewRedis(args.id, duration=args.duration)


@utils.arg('id', metavar='<ID>', help='ID of redis')
@utils.arg('memory', metavar='<MEMORY>', help='Redis memory size(GB)')
@utils.arg('--duration', metavar='<DURATION>', help='Reserved redis duration, in H or M, e.g. 72H, 1M')
def do_ChangeRedisType(client, args):
    """ Change Redis type """
    client.ChangeRedisType(args.id, args.memory, duration=args.duration)


@utils.arg('id', metavar='<ID>', help='ID of redis')
def do_GetRedisContractInfo(client, args):
    """ Query redis contract information """
    val = client.GetRedisContractInfo(args.id)
    utils.print_dict(val)
