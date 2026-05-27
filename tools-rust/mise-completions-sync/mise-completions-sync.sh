for f in ${XDG_DATA_HOME:-$HOME/.local/share}/mise-completions/bash/*; do
	[[ -f "$f" ]] && source "$f"
done
