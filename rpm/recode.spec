Name:       recode

Summary:    Conversion between character sets and surfaces
Version:    3.6
Release:    1
License:    GPLv2+
URL:        https://github.com/sailfishos/recode
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
The `recode' converts files between character sets and usages.
It recognises or produces nearly 150 different character sets
and is able to transliterate files between almost any pair. When exact
transliteration are not possible, it may get rid of the offending
characters or fall back on approximations.  Most RFC 1345 character sets
are supported.


%package devel
Summary:    Header files and static libraries for development using recode
Requires:   %{name} = %{version}-%{release}

%description devel
The `recode' library converts files between character sets and usages.
The library recognises or produces nearly 150 different character sets
and is able to transliterate files between almost any pair. When exact
transliteration are not possible, it may get rid of the offending
characters or fall back on approximations. Most RFC 1345 character sets
are supported.


%prep
%setup -q -n %{name}-%{version}/%{name}
./after-patch.sh

%build
%configure --disable-static
%make_build

%install
%make_install
%find_lang recode

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f recode.lang
%defattr(-,root,root,-)
%license COPYING*
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc %{_mandir}/*/*
%doc %{_infodir}/recode.info*
%{_bindir}/*
%{_libdir}/librecode.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/librecode.so
