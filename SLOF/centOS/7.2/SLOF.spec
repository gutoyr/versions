Name:           SLOF
Version:        20160525
Release:        3%{?dist}
Summary:        Slimline Open Firmware

License:        BSD
URL:            http://www.openfirmware.info/SLOF
BuildArch:      noarch

Source0:        SLOF.tar.gz

# LTC: building native; no need for xcompiler
BuildRequires:  perl(Data::Dumper)


%description
Slimline Open Firmware (SLOF) is initialization and boot source code
based on the IEEE-1275 (Open Firmware) standard, developed by
engineers of the IBM Corporation.

The SLOF source code provides illustrates what's needed to initialize
and boot Linux or a hypervisor on the industry Open Firmware boot
standard.

Note that you normally wouldn't need to install this package
separately.  It is a dependency of qemu-system-ppc64.


%prep
%setup -q -n SLOF

if test -r "gitlog" ; then
    echo "This is the first 50 lines of a gitlog taken at archive creation time:"
    head -50 gitlog
    echo "End of first 50 lines of gitlog."
fi

%build
export CROSS=""
make qemu %{?_smp_mflags} V=2


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/qemu
cp -a boot_rom.bin $RPM_BUILD_ROOT%{_datadir}/qemu/slof.bin


%files
%doc FlashingSLOF.pdf
%doc LICENSE
%doc README
%dir %{_datadir}/qemu
%{_datadir}/qemu/slof.bin


%changelog
* Thu Nov 3 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 20160525-3
- Spec cleanup

* Tue Aug 30 2016 Mauro S. M. Rodrigues <maurosr@linux.vnet.ibm.com> - 20160525-2.1
- Build August, 24th, 2016

* Tue Sep 10 2013 baseuser@ibm.com
- Base-8.x spec file
