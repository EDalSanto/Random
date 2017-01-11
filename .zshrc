# aliases
alias cl='clear'
alias compile='gcc -Wall -Wextra -Werror -g'
alias compilem='gcc -Wall -Wextra -Werror -g -fsanitize=address'
alias run='./a.out'
alias mc='make re && make clean'

# git aliases
alias gst='git status'
alias gc='git commit -m'
alias ga='git add'
alias gp='git push'

# color commands
alias grep='grep --colour=auto'
alias fgrep='fgrep --colour=auto'
alias egrep='egrep --colour=auto'

# prompt
PROMPT='[%1~]$ '

export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
