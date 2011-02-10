<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>metadata</key>
    <dict>
        <key>fontname</key>
        <string>${metadata['fontname']}</string>
        <key>fontsize</key>
        <real>${metadata['fontsize']}</real>
        <key>width</key>
        <real>${metadata['width']}</real>
        <key>height</key>
        <real>${metadata['height']}</real>
        <key>padding</key>
        <real>${metadata['padding']}</real>
    </dict>
    <key>characters</key>
    <dict>
        % for character in characters:
        <key>${character['name'] | x}</key>
        <dict>
            <key>x</key>
            <real>${character['x']}</real>
            <key>y</key>
            <real>${character['y']}</real>
            <key>width</key>
            <real>${character['width']}</real>
            <key>height</key>
            <real>${character['height']}</real>
            <key>xbearing</key>
            <real>${character['xbearing']}</real>
            <key>ybearing</key>
            <real>${character['ybearing']}</real>
            <key>xadvance</key>
            <real>${character['xadvance']}</real>
            <key>yadvance</key>
            <real>${character['yadvance']}</real>    
        </dict>
        % endfor
    </dict>
</dict>
</plist>
