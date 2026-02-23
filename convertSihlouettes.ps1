# Rename files by replacing spaces with underscores
Get-ChildItem -File | ForEach-Object {
    $newName = $_.Name -replace ' ', '_'
    Rename-Item -Path $_.FullName -NewName $newName
}

# Trim whitespace from PNG images
magick mogrify -format png -fuzz 0% -trim +repage *.png


# Center images on a square canvas
Get-ChildItem -Filter *.png | ForEach-Object {
    # Get image dimensions using ImageMagick
    $info = magick identify -format "%w %h" $_.FullName
    $width, $height = $info -split " "
    
    # Determine the maximum dimension
    $maxDim = [math]::Max([int]$width, [int]$height)

    # Apply extent to ensure a square canvas
    magick convert $_.FullName -gravity Center -background White -extent "${maxDim}x${maxDim}" $_.FullName
}


# Resize images to 500x500
magick mogrify -format png -resize 500x500 *.png

# Add a white border to images
magick mogrify -format png -bordercolor white -border 25 *.png

# Resize images to 100x100 and apply a threshold
magick mogrify -format png -resize 100x100 -threshold 50% *.png