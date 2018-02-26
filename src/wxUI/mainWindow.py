# -*- coding: utf-8 -*-
import wx
import wx.adv
import application
import widgetUtils

class mainWindow(wx.Frame):
	def makeMenu(self):
		mb = wx.MenuBar()
#		app_ = wx.Menu()
#		mb.Append(app_, _(u"Application"))
		player = wx.Menu()
		self.player_play = player.Append(wx.NewId(), _(u"Play"))
		self.player_stop = player.Append(wx.NewId(), _(u"Stop"))
		self.player_previous = player.Append(wx.NewId(), _(u"Previous"))
		self.player_next = player.Append(wx.NewId(), _(u"Next"))
		self.player_shuffle = player.AppendCheckItem(wx.NewId(), _(u"Shuffle"))
		self.player_volume_down = player.Append(wx.NewId(), _(u"Volume down"))
		self.player_volume_up = player.Append(wx.NewId(), _(u"Volume up"))
		self.player_mute = player.Append(wx.NewId(), _(u"Mute"))
		help_ = wx.Menu()
		self.about = help_.Append(wx.NewId(), _(u"About {0}").format(application.name,))
		self.check_for_updates = help_.Append(wx.NewId(), _(u"Check for updates"))
		self.website = help_.Append(wx.NewId(), _("Visit website"))
		mb.Append(player, _(u"Player"))
		mb.Append(help_, _(u"Help"))
		self.SetMenuBar(mb)

	def __init__(self):
		super(mainWindow, self).__init__(parent=None, id=wx.NewId(), title=application.name)
		self.Maximize(True)
		self.makeMenu()
		self.panel = wx.Panel(self)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sb = self.CreateStatusBar()
		lbl2 = wx.StaticText(self.panel, wx.NewId(), _(u"search"))
		self.text = wx.TextCtrl(self.panel, wx.NewId())
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(lbl2, 0, wx.GROW)
		box.Add(self.text, 1, wx.GROW)
		box.Add(wx.StaticText(self.panel, wx.NewId(), _("Search in")), 0, wx.GROW)
		self.extractor = wx.ComboBox(self.panel, wx.NewId(), choices=["youtube", "zaycev.net"], value="youtube", style=wx.CB_READONLY)
		box.Add(self.extractor, 1, wx.GROW)
		self.search = wx.Button(self.panel, wx.NewId(), _("Search"))
		self.search.SetDefault()
		box.Add(self.search, 0, wx.GROW)
		self.sizer.Add(box, 0, wx.GROW)
		lbl = wx.StaticText(self.panel, wx.NewId(), _("Results"))
		self.list = wx.ListBox(self.panel, wx.NewId())
		self.sizer.Add(lbl, 0, wx.GROW)
		self.sizer.Add(self.list, 1, wx.GROW)
		box1 = wx.BoxSizer(wx.HORIZONTAL)
		box2 = wx.BoxSizer(wx.HORIZONTAL)
		box1.Add(wx.StaticText(self.panel, wx.NewId(), _("Position")), 0, wx.GROW)
		self.time_slider = wx.Slider(self.panel, -1)
		box1.Add(self.time_slider, 1, wx.GROW)
		box1.Add(wx.StaticText(self.panel, wx.NewId(), _("Volume")), 0, wx.GROW)
		self.vol_slider = wx.Slider(self.panel, -1, 0, 0, 100, size=(100, -1))
		box1.Add(self.vol_slider, 1, wx.GROW)
		self.previous = wx.Button(self.panel, wx.NewId(), _("Previous"))
		self.play  = wx.Button(self.panel, wx.NewId(), _("Play"))
		self.stop   = wx.Button(self.panel, wx.NewId(), _("Stop"))
		self.next = wx.Button(self.panel, wx.NewId(), _("Next"))
		box2.Add(self.previous)
		box2.Add(self.play, flag=wx.RIGHT, border=5)
		box2.Add(self.stop)
		box2.Add(self.next)
		self.sizer.Add(box1, 0, wx.GROW)
		self.sizer.Add(box2, 1, wx.GROW)
		self.panel.SetSizerAndFit(self.sizer)
#		self.SetClientSize(self.sizer.CalcMin())
#		self.Layout()
#		self.SetSize(self.GetBestSize())

	def change_status(self, status):
		self.sb.SetStatusText(status)

	def about_dialog(self, *args, **kwargs):
		info = wx.adv.AboutDialogInfo()
		info.SetName(application.name)
		info.SetVersion(application.version)
		info.SetDescription(application.description)
		info.SetCopyright(application.copyright)
		info.SetWebSite(application.url)
#		info.SetTranslators(application.translators)
#  info.SetLicence(application.licence)
		info.AddDeveloper(application.author)
		wx.adv.AboutBox(info)

	def get_text(self):
		t = self.text.GetValue()
		self.text.ChangeValue("")
		return t

	def get_item(self):
		return self.list.GetSelection()

	def get_destination_path(self, filename):
		saveFileDialog = wx.FileDialog(self, _(u"Save this file"), "", filename, _(u"Audio Files(*.mp3)|*.mp3"), wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if saveFileDialog.ShowModal() == wx.ID_OK:
			return saveFileDialog.GetPath()
		saveFileDialog.Destroy()