#! /usr/bin/perl

use 5.010;
use strict;
use warnings;
use Carp;
use Device::USB;
use Device::USB::PCSensor::HidTEMPer::Device;
use Device::USB::PCSensor::HidTEMPer::NTC;
use Device::USB::PCSensor::HidTEMPer::TEMPer; 
use lib;
use Device::USB::PCSensor::HidTEMPer;

my $pcsensor  = Device::USB::PCSensor::HidTEMPer->new();
my @devices   = $pcsensor->list_devices();
  
foreach my $device ( @devices )
   {
   say $device->internal()->celsius();
   }