#!/bin/sh
readonly DEBUG=0
[ -z $1 ] && echo "$0 IP" && exit 0
HOST=$1
readonly APP_ID="cli_a07c20f45379500d"
readonly APP_SECRET="bTfO1pJLOejnNWXmgvx2ehuNEyMGfeQT"
readonly FS_URL="https://open.feishu.cn/open-apis"
readonly SHEET_TOKEN="shtcnG6DDCZgyZpO1TT1eDRvnjd"
readonly APP_TOKEN=$(curl -s -X POST "$FS_URL/auth/v3/tenant_access_token/internal" -H "content-type:application/json; charset=utf-8" -d '{ "app_id": "'"$APP_ID"'", "app_secret": "'"$APP_SECRET"'" }' | jq -r '.tenant_access_token')
readonly HEADER="Authorization: Bearer $APP_TOKEN"
[ $DEBUG = 1 ] && echo $HEADER
readonly SHEET_ID=$(curl -s -X GET "$FS_URL/sheets/v2/spreadsheets/$SHEET_TOKEN/metainfo?extFields=protectedRange&user_id_type=open_id" -H "$HEADER" | jq -r '.data.sheets[0].sheetId')
[ $DEBUG = 1 ] && echo $SHEET_ID


ROW=$(curl -s -q -X POST "$FS_URL/sheets/v3/spreadsheets/$SHEET_TOKEN/sheets/$SHEET_ID/find" \
-H "$HEADER" -H "content-type:application/json; charset=utf-8" -d '{
"find_condition": {
         "range": "'"$SHEET_ID"'",
         "match_case": true,
         "match_entire_cell": false,
         "search_by_regex": false,
         "include_formulas": false
     },
     "find": "'"$HOST"'"
}' |  jq -r '.data.find_result.matched_cells[]' | sed -r -n 's@[A-Za-z]@@gp')
[ $DEBUG = 1 ] && echo $ROW
if [ -z $ROW ];then
echo "$HOST:No such host."
else
#echo -en "$HOST:"
#curl -s -X GET "$FS_URL/sheets/v2/spreadsheets/$SHEET_TOKEN/values/$SHEET_ID!A$ROW:B$ROW?valueRenderOption=ToString&dateTimeRenderOption=FormattedString" -H "$HEADER" -H "content-type:application/json; charset=utf-8"  | jq '.data.valueRange.values[][]' | tr '[\r\n"]' '-'
curl -s -X GET "$FS_URL/sheets/v2/spreadsheets/$SHEET_TOKEN/values/$SHEET_ID!A$ROW:B$ROW?valueRenderOption=ToString&dateTimeRenderOption=FormattedString" -H "$HEADER" -H "content-type:application/json; charset=utf-8"
fi