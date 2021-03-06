%global commit0 9f0833886e76c52bb9f30861c72972ec25f82585
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           cmus
Version:        2.9.1
Release:        7%{?gver}%{dist}
Summary:        Ncurses-Based Music Player

License:        GPLv2+
URL:            https://cmus.github.io/
Source0:        https://github.com/cmus/cmus/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  faad2-devel >= 2.9.1
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libdiscid)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  libmpcdec-devel
BuildRequires:  libmp4v2-devel
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wavpack)

%description
Small, fast and powerful console music player for Unix-like operating systems.
                                                                             
%prep
%autosetup -n %{name}-%{commit0}  

%build
./configure \
        prefix=%{_prefix} \
        libdir=%{_libdir} \
        CFLAGS="%{optflags}" \
        CONFIG_MIKMOD=y \
        CONFIG_VTX=n \
        CONFIG_ROAR=n \
        CONFIG_ARTS=n \
        CONFIG_SUN=n

%make_build V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT

mv %{buildroot}%{_docdir}/%{name}/examples .

mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -pm 0644 contrib/%{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/

%files
%doc AUTHORS README.md examples
%license COPYING
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}.bash-completion
%{_bindir}/%{name}
%{_bindir}/%{name}-remote
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-remote.1.*
%{_mandir}/man7/%{name}-tutorial.7.*

%changelog

* Sun Jan 24 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.9.1-7.git9f08338
- Updated to 2.9.1

* Sat Nov 09 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.8.0-7.git354625c
- Updated to current commit
- Rebuilt for faad2

* Thu Jan 18 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.8.0-3.git15b5c5b
- Updated to 2.8.0-3.git15b5c5b

* Sun Dec 10 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.8.0-2.gitcbaf983
- Updated to 2.8.0-2.gitcbaf983

* Sun Jun 26 2016 The UnitedRPMs Project (Key for UnitedRPMs infrastructure) <unitedrpms@protonmail.com> - 2.7.1-6
- Rebuild with new ffmpeg

* Mon Nov 30 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-5.R
- add V=2 (Make the build verbose)
- use pkgconfig for BuildRequires
- use proper CFLAGS

* Sat Oct 31 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-4.R
- move examples to right path

* Thu Oct 22 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-3.R
- add BR libcdio-paranoia-devel
- add BR libmikmod-devel
- add %%make_build
- remove make %%{?_smp_mflags} V=2
- cleanup spec

* Thu Sep 03 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-2.R
- remove BuildRequires: arts-devel

* Wed Sep 02 2015 Maxim Orlov <murmansksity@gmail.com> - 2.7.1-1.R
- Initial package.
