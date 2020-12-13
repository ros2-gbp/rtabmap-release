/*
Copyright (c) 2010-2016, Mathieu Labbe - IntRoLab - Universite de Sherbrooke
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Universite de Sherbrooke nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#pragma once

#include "rtabmap/core/RtabmapExp.h" // DLL export/import defines

#include "rtabmap/core/StereoCameraModel.h"
#include "rtabmap/core/Camera.h"
#include "rtabmap/core/Version.h"

namespace libfreenect2
{
class Freenect2;
class Freenect2Device;
class SyncMultiFrameListener;
class Registration;
class PacketPipeline;
}

namespace rtabmap
{

class RTABMAP_EXP CameraFreenect2 :
	public Camera
{
public:
	static bool available();

	enum Type{
		kTypeColor2DepthSD,
		kTypeDepth2ColorSD,
		kTypeDepth2ColorHD,
		kTypeDepth2ColorHD2,
		kTypeIRDepth,
		kTypeColorIR
	};

public:
	// default local transform z in, x right, y down));
	CameraFreenect2(int deviceId= 0,
					Type type = kTypeDepth2ColorSD,
					float imageRate=0.0f,
					const Transform & localTransform = CameraModel::opticalRotation(),
					float minDepth = 0.3f,
					float maxDepth = 12.0f,
					bool bilateralFiltering = true,
					bool edgeAwareFiltering = true,
					bool noiseFiltering = true,
					const std::string & pipelineName = "");
	virtual ~CameraFreenect2();

	virtual bool init(const std::string & calibrationFolder = ".", const std::string & cameraName = "");
	virtual bool isCalibrated() const;
	virtual std::string getSerial() const;

protected:
	virtual SensorData captureImage(CameraInfo * info = 0);

private:
#ifdef RTABMAP_FREENECT2
	int deviceId_;
	Type type_;
	StereoCameraModel stereoModel_;
	libfreenect2::Freenect2 * freenect2_;
	libfreenect2::Freenect2Device *dev_;
	libfreenect2::SyncMultiFrameListener * listener_;
	libfreenect2::Registration * reg_;
	float minKinect2Depth_;
	float maxKinect2Depth_;
	bool bilateralFiltering_;
	bool edgeAwareFiltering_;
	bool noiseFiltering_;
	std::string pipelineName_;
#endif
};


} // namespace rtabmap
