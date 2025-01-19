class en:
	xcoder = 'SCryptor | Version: %s'
	detected_os = 'Detected %s OS.'
	installing = 'Installing required modules...'
	crt_workspace = 'Creating workspace directories...'
	verifying = 'Verifying installation...'
	installed = '%s was sucessfully installed!'
	not_installed = '%s wasn\'t installed!'
	clear_qu = 'Are you sure you want to clear the dirs?'
	done = 'Done!'
	choice = 'Your choice: '
	to_continue = 'Press Enter to continue...'
	expiremental = 'Experimental feature'
	sc = 'SC'
	dsc = 'Decode SC'
	dsc_desc = 'Convert SC to PNG'
	esc = 'Encode SC'
	esc_desc = 'Convert PNG to SC'
	d1sc = 'Decode SC to chunks'
	e1sc = 'Encode SC from chunks'
	oth = 'OTHER'
	chkupd = 'Check for updates'
	version = 'Current version: %s'
	credits = 'Credits'
	relang = 'Select another language'
	relang_desc = 'Current lang: %s'
	clean_dirs = 'Clear workspace dirs'
	clean_dirs_desc = 'Clear In and Out dirs'
	exit = 'Exit'
	done_err = 'DONE WITH %s ERRORS!\nFor more information check log.txt'
	got_error = 'Got error: \n%s\n\n'
	collecting_inf = 'Collecting information...'
	about_sc = 'About: FileName: %s, FileType: %s, FileSize: %s, SubType: %s, Width: %s, Height: %s'
	try_error = 'Error while decompessing! Trying to decode as is...'
	not_installed2 = '%s isn\'t installed! Return'
	decomp_err = 'Decompression failed'
	detected_comp = 'Detected %s compression!'
	unk_type = 'Unknown pixel type: %s'
	crt_pic = 'Creating picture...'
	join_pic = 'Joining picture...'
	png_save = 'Saving to png...'
	saved = 'Saving completed!'
	not_xcod = '.xcod file doesn\'t exist!'
	standart_types = 'We will use standart fileType and subType (1, 0).\n       And also LZMA compression (as in Brawl Stars sc)'
	illegal_size = 'Illegal image size! Expected %sx%s but we got %sx%s'
	resize_qu = 'Would you like to resize an image?'
	resizing = 'Resizing...'
	split_pic = 'Splitting picture...'
	writing_pic = 'Writing pixels...'
	header_done = 'Header wrote!'
	comp_with = 'Compressing texture with %s...'
	comp_err = 'Compression failed'
	comp_done = 'Compression done!'
	dir_empty = 'Dir \'%s\' is empty!'
	not_found = '\'%s\' file isn\'t found!'
	cut_sprites = 'Cutting sprites... (%s/%s)'
	place_sprites = 'Placing sprites... (%s/%s)'
	not_implemented = 'This feature will be added in future updates.\nYou can follow XCoder updates here: github.com/MasterDevX/XCoder'
	want_exit = 'Want to exit?'
	dec_sc = 'Decoding .sc file...'
	dec_sctex = 'Decoding _tex.sc file...'
	err = 'ERROR! (%s.%s: %s)'

string = {'en': en}

def center_2strings(conwidth, str1, str2):
	return print(str1 + (' ' * (conwidth // 2 - len(str1)) + '-> ' + str2))

def colored_str(text):
	return print(colorama.Fore.GREEN + text + ' ' * (10 - len(text)) + colorama.Style.RESET_ALL)

def console(config):
	global colorama
	s = string[config['lang']]
	from system.Lib import colorama, shutil
	conwidth = shutil.get_terminal_size().columns
	print()
	print((colorama.Back.BLACK + colorama.Fore.GREEN + s.xcoder % config['version'] + colorama.Style.RESET_ALL).center(conwidth + 14))
	print('github.com/Nexustwm/SCryptor'.center(conwidth))
	print()
	colored_str(s.sc)
	center_2strings(conwidth, ' 1   ' + s.dsc, s.dsc_desc)
	center_2strings(conwidth, ' 2   ' + s.esc, s.esc_desc)
	center_2strings(conwidth, ' 3   ' + s.d1sc, s.expiremental)
	center_2strings(conwidth, ' 4   ' + s.e1sc, s.expiremental)
	print()
	colored_str(s.oth)
	center_2strings(conwidth, ' 5 ' + s.clean_dirs, s.clean_dirs_desc)
	print(' 6 ' + s.credits)
	print(' 7 ' + s.exit)
	print()
	choice = input(s.choice)
	print()
	return choice



