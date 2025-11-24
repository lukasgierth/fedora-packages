%global debug_package %{nil}

Name:       grype
# renovate: datasource=github-releases depName=anchore/grype extractVersion=true
Version:    0.104.0
Release:    1%{?dist}
Summary:    A vulnerability scanner for container images and filesystems
License:    Apache-2.0
URL:        https://github.com/anchore/grype
Source:     %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: git-core
BuildRequires: go-md2man
BuildRequires: golang >= 1.24.1

%description

%prep
%autosetup -n %{name}-%{version}

%build
go build \
    -ldflags "-X main.version=%{version} -s -w" \
    -o _build/%{name} \
    ./cmd/%{name}

go-md2man -in README.md -out %{name}.1

%install
install -Dpm 0755 _build/%{name} -t %{buildroot}%{_bindir}
install -Dpm 0644 %{name}.1 -t %{buildroot}/%{_mandir}/man1/

install -d %{buildroot}%{bash_completions_dir}
install -d %{buildroot}%{fish_completions_dir}
install -d %{buildroot}%{zsh_completions_dir}
_build/%{name} completion bash > %{buildroot}%{bash_completions_dir}/grype
_build/%{name} completion fish > %{buildroot}%{fish_completions_dir}/grype.fish
_build/%{name} completion zsh > %{buildroot}%{zsh_completions_dir}/_grype


%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*
%{bash_completions_dir}/grype
%{fish_completions_dir}/grype.fish
%{zsh_completions_dir}/_grype

%changelog
%autochangelog
