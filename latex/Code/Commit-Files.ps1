#########################################################################
# This PowerShell-script commits all changes to the current repository. #
# Author: Anton Plagemann (anton.plagemann@dxc.com)                     #
# Version: 1.0 (06.08.2021)                                             #
#########################################################################

# Configure git user details (committing user)
git config --global user.email "pipeline@azure.com"
git config --global user.name "Azure Pipeline User"

# Add everything and commit
git add *
$date = [System.TimeZoneInfo]::ConvertTimeBySystemTimeZoneId((Get-Date), 'Romance Standard Time').ToString('yyyy-MM-dd HH:mm:ss')
git commit -m "$env:COMMITMESSAGE ($date)"

# Push changes
git push origin
