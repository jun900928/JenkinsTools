# For descriptions of keys, please refer to README.txt

# Product configuration for 'victara_verizon_adr'
my $prod_config =
{
 'make_command'       =>
 {
    'continuous' =>
    {
        'userdebug' => q(motorola/build/bin/build_device.bash -p victara_verizon_adr -g),
    },
    'derivative' =>
    {
        'userdebug' => q(motorola/build/bin/build_device.bash -p victara_verizon_adr -g),
    },
 },
 'mbm_rel_notes'      => q(/------------/32452345/-@#$%^asdf/asfadsf/asdfasdf/*(/prebuilt/mbm/ReleaseNotes.txt),
 'ota_info'           =>
 {
    'userdebug' =>
    {
        'incremental' => TRUE,
    },
 },
 'release_team_email' => q(xplus1rsw gbf437),
};
