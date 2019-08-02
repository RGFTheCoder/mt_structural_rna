import csv
import os
import argparse

parser = argparse.ArgumentParser(description="sets file name")
parser.add_argument("startfile", help="Enter name of data file")
parser.add_argument("destination", help="Enter name of destination file")
args = parser.parse_args()

if os.path.exists(args.startfile) and os.path.exists(args.destination):
	print "All files exist--running program"

	with open(args.startfile) as tsv:
		reader = csv.DictReader(tsv, delimiter="\t")
		with open(args.destination, 'w') as f:

			f.write('<svg height="2000" width="3000" xmlns="http://www.w3.org/2000/svg">\n\n')
			f.write('\n<!-- MARKERS -->\n')
			
			for row in reader:
				infoType = row["Type"]
				genCoord = row["Genomic_Coordinate"]
				base = row["Base"]
				x1 = row["x1"]
				y1 = row["y1"]
				x2 = row["x2"]
				y2 = row["y2"]
				textColor = "#000000"
				font = "monospace"
				fontWeight = 'normal'
				title = genCoord
				lineColor = "#2975d9"  # blue
				circleColor = "#b30000"  # red
				with open('pop_data.txt') as tsv:
					reader = csv.DictReader(tsv, delimiter="\t")
					print ('processing population data...')
					if infoType == "b":
						for row in reader:
							chrom = row["#CHROM"]
							mutCoord = row["POS"]
							ref = row["REF"]
							mutation = row["ALT"]
							result = [chrom, mutCoord, ref, mutation]
							if (int(mutCoord) - int(genCoord)) == 0:
								textColor = 'red'

				if infoType == "b":
					f.write('<text x="' + x1 + '" y="' + y1 + '" style = "font-size: 12; fill: ' + textColor + '; font-family: ' + font + '; font-weight: ' + fontWeight + ';" > ' + base + '<title>' + title + '</title> </text>')
				elif infoType == "l":
					f.write('<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" style="stroke: '	+ lineColor + '; stroke-width:1; stroke-linecap: round" >' + '<title>' + x1 + ',' + y1
							+ " " + x2 + "," + y2 + '</title> </line>')
				elif infoType == "d":
					f.write('<circle cx="' + x1 + '" cy="' + y1 + '" r="2" style="fill: ' + circleColor + ';" >' + '<title>' + x1 + ',' + y1 + '</title> </circle>')
			f.write('</svg>')
		
			print "Finished"

else:
	print "error"
