Summary:	Realistic sky generator
Summary(pl):	Realistyczny generator obrazu nieba
Name:		stellarium
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/stellarium/%{name}-%{version}.tar.gz
# Source0-md5:	f00e99b88f53273419683cf18905e39c
# Source0-size:	9431913
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-autoconf.patch
URL:		http://stellarium.free.fr/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stellarium renders 3D realistic skies in real time with OpenGL. It
displays stars, constellations, planets, nebulas and others things
like ground, landscape, fog, etc. Main features:
- Over 120000 stars from the Hipparcos Catalogue with name and infos
  for the brightest ones.
- Planets in real time, with a powerfull zoom mode.
- Drawing of the 88 constellations with their names.
- More than 40 messiers objects (Orion, M31 etc..).
- Photorealistic Milky Way.
- Ground, fog, and landscape.
- Star twinkling.
- Time control (real time and accelered time modes).
- Clikable stars, planets and nebulas with informations.
- Smooth real time navigation.
- Windowed and fullscreen modes.

%description -l pl
Stellarium przy pomocy OpenGL-a oddaje w czasie rzeczywistym
trójwymiarowe, realistyczne obrazy nieba. Wy¶wietla gwiazdy,
konstelacje, planety, nebule i inne obiekty takie jak powierzchnia
ziemi, krajobrazy, mg³a, itp. G³ówne cechy to:
- Ponad 120000 gwiazd z "Hipparcos Catalogue" z nazwami i opisem
  najja¶niejszych.
- Planety w czasie rzeczywistym z mo¿liwo¶ci± du¿ego powiêkszania.
- Wy¶wietlanie 88 konstelacji wraz z ich nazwami.
- Ponad 40 obiektów messiera (Orion, M31, itp...).
- Realistyczna Droga Mleczna.
- Powierzchnia, mg³a i krajobraz.
- Migotanie gwiazd.
- Kontrola czasu (tryby czasu rzeczywistego i przy¶pieszonego).
- Dostêp do informacji na temat gwiazd, planet i nebuli po ich
  klikniêciu.
- P³ynna nawigacja w czasie rzeczywistym.
- Tryb pracy pe³noekranowej i w oknie.

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_pixmapsdir}/%{name}.png
