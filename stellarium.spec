Summary:	Stellarium photo-realistic sky generator
Summary(pl):	Stellarium
Name:		stellarium
Version:	0.5.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
# Source0-md5:	3765a5ba8cb0e328ccccc282e21c875e
#Source1:	%{name}.desktop
Patch0:		%{name}-etc.patch
URL:		http://stellarium.free.fr/
BuildRequires:	SDL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stellarium renders 3D photo-realistic skies in real time with OpenGL.
It displays stars, constellations, planets, nebulas and others things
like ground, landscape, fog, etc.
    - Over 120000 stars from the Hipparcos Catalogue with name and infos
      for the brightest ones.
    - Planets in real time, with a powerfull zoom mode to see them like in
      a telescope.
    - Drawing of the 88 constellations with their names.
    - Drawing of more than 40 messiers objects (Orion, M31 etc..).
    - Photorealistic Milky Way.
    - Ground, fog, and landscape.
    - Star twinkling.
    - Grids in Equatorial and Azimuthal coordinates.
    - Time control (real time and accelered time modes).
    - Graphical menu for simple utilisation.
    - Clikable stars, planets and nebulas with informations.
    - Ecliptic and celestrial equator lines.
    - Smooth real time navigation.
    - Windowed and fullscreen modes.


%description -l pl

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-sdltest
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_sysconfdir}/X11/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/config/* \
	$RPM_BUILD_ROOT%{_sysconfdir}/X11/%{name}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/%{name}
%{_datadir}/%{name}
#%{_desktopdir}/%{name}.desktop
