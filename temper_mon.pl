#!/usr/bin/perl
use strict;
use Device::USB::PCSensor::HidTEMPer;

my $pcsensor  = Device::USB::PCSensor::HidTEMPer->new();
my @devices   = $pcsensor->list_devices();

foreach my $device (@devices) {
	printf "Sensor Temperature C: %s\n", $device->internal()->celsius();
}
